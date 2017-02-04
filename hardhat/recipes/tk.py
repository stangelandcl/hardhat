import os
from .base import GnuRecipe
from ..util import patch
from ..version import extension_regex


class TkRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TkRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fbbd93541b4cd467841208643b4014c4' \
                      '543a54c3597586727f0ab128220d7946'

        self.name = 'tk'
        self.depends = ['tcl', 'xorg-libs']
        self.version = '8.6.5'
        self.version_regex = self.name + r'(?P<version>\d+d.\d+\.\d+)-src' \
            + extension_regex
        self.version_url = 'https://tcl.tk/software/tcltk/download.html'
        self.url = 'http://downloads.sourceforge.net/tcl/' \
                   '$name$version-src.tar.gz'

        self.configure_strip_cross_compile()
        self.configure_args += ['--enable-64bit']
        self.environment['LIBS'] += ' -lm'
        self.install_args = [
            self.install_args,
            ['make', 'install-private-headers'],
            ['ln', '-v', '-sf', 'wish8.6', '%s/bin/wish' % self.prefix_dir]]

    @property
    def directory(self):
        d = super(TkRecipe, self).directory
        return os.path.join(d, 'unix')

    def compile(self):
        try:
            super(TkRecipe, self).compile()
        except Exception as e:
            print('ignoring compile error: %s' % e)

        src = r'''TK_SRC_DIR='%s/build/tk-%s''' % (self.prefix_dir,
                                                   self.short_version)
        dst = r'''TK_SRC_DIR='%s/include''' % self.prefix_dir
        filename = os.path.join(self.directory, 'tkConfig.sh')
        patch(filename, src, dst)

        src = r'%s/build/tk-%s/unix' % (self.prefix_dir, self.short_version)
        dst = r'%s/lib' % self.prefix_dir
        patch(filename, src, dst)
