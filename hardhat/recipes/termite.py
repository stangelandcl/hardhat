import os
from .base import GnuRecipe


class TermiteRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TermiteRecipe, self).__init__(*args, **kwargs)
        self.name = 'termite'
        self.version = '13'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'pcre2', 'vte-ng']
        self.version_url = 'https://github.com/thestinger/termite/releases'
#        self.url = 'https://github.com/thestinger/termite/archive/v$version.tar.gz'
        self.url = 'https://github.com/thestinger/termite.git'
        self.compile_args += ['VERSION=%s' % self.version]
        self.install_args += ['DESTDIR=%s' % self.prefix_dir,
                              'PREFIX=""']

    def configure(self):
        pass

    def download(self):
        self.log_dir('download', self.directory, 'git clone')
        args = ('git clone --recursive %s %s' % (
            self.url, os.path.basename(self.directory))).split()
        self.run_exe(args, os.path.dirname(self.directory), self.environment)
