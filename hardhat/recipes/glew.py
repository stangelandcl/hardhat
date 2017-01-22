import os
from .base import GnuRecipe
from ..version import extension_regex


class GlewRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GlewRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f7ad0b2629fb4cd591a3c1a490448e7e' \
                      '0409cc4ae79c578a09b4884304e01574'

        self.name = 'glew'
        self.version = '2.0.0'
        self.version_regex = self.name + r'-(?P<version>\d+\.\d+\.\d+)' \
            + extension_regex
        self.depends = ['mesa']
        self.url = 'https://github.com/nigels-com/$name/archive/' \
                   '$name-$version.tar.gz'

        self.configure_args = ['make',
                               'GLEW_DEST=%s' % self.prefix_dir,
                               'SYSTEM=linux',
                               'LDFLAGS.EXTRA=""']
        self.compile_args = ['make', 'all',
                             'GLEW_DEST=%s' % self.prefix_dir,
                             'SYSTEM=linux',
                             'LDFLAGS.EXTRA=""']
        self.install_args += ['GLEW_DEST=%s' % self.prefix_dir,
                              'SYSTEM=linux',
                              'LDFLAGS.EXTRA=""']

    def configure(self):
        self.log_dir('configure', self.directory, 'configure')
        self.run_exe(self.configure_args,
                     os.path.join(self.directory, 'auto'),
                     self.environment)
