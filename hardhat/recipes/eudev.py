import os
from .base import GnuRecipe
from ..util import patch


class EudevRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(EudevRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '57e3d9e51cfefbdad431848ea0ad8ae1' \
                      'cde04928da42474f44bd200b12f5fe19'

        self.name = 'eudev'
        self.version = '3.2.1'
        self.url = 'http://dev.gentoo.org/~blueness/eudev/' \
                   'eudev-$version.tar.gz'
        self.depends = ['gperf']
        self.configure_args += ['--enable-manpages']

    def _patch(self, filename, text):
        with open(filename, 'rt') as f:
            file_text = text + f.read()
        with open(filename, 'wt') as f:
            f.write(file_text)

    def patch(self):
        self.log_dir('patch', self.directory,
                     'adding BTN_TRIGGER_HAPPY and INPUT_PROP_MAX')
        text = """
#ifndef BTN_TRIGGER_HAPPY
#define BTN_TRIGGER_HAPPY (0x2c0)
#endif

#ifndef INPUT_PROP_MAX
#define INPUT_PROP_MAX (0x1f)
#endif

"""
        filename = os.path.join(self.directory,
                                'src/udev/udev-builtin-input_id.c')
        self._patch(filename, text)

        self.log_dir('patch', self.directory,
                     'removing duplicate declaration')
        src = r'static const struct key *keyboard_lookup_key' \
              '(const char *str, unsigned len);'
        filename = os.path.join(self.directory,
                                'src/udev/udev-builtin-keyboard.c')
        patch(filename, src, '')

    def install(self):
        super(EudevRecipe, self).install()
        self.install_args = ['udevadm',
                             'hwdb',
                             '--update']
        super(EudevRecipe, self).install()

#    def patch(self):
#        cache = os.path.join(self.directory, 'config.cache')
#        text = '''
#HAVE_BLKID=1
#BLKID_LIBS="-lblkid"
#BLKID_CFLAGS=""
#'''
#        with open(cache, 'wt') as f:
#            f.write(text)
