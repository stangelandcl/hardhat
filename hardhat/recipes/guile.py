import os
from .base import GnuRecipe
from hardhat.urls import Urls


class GuileRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GuileRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '33b904c0bf4e48e156f3fb1d0e6b0392' \
                      '033bd610c6c9d9a0410c6e0ea96a3e5c'

        self.name = 'guile'
        self.version = '2.2.4'
        self.url = Urls.gnu_template(self.name, self.version)
        self.depends = ['bash', 'coreutils', 'gc', 'gmp', 'libffi',
                        'libtool', 'libunistring', 'ncurses', 'readline']
        # to avoid requiring a bootstrap guile
        self.configure_strip_cross_compile()

    def extract(self):
        if not os.path.exists(self.extract_dir):
            os.makedirs(self.extract_dir)
        args = ['tar', 'xf', self.filename, '--strip-components=1',
                '-C', self.directory]
        self.log_dir('extract', self.directory,
                     'extract %s' % self.filename)
        self.run_exe(args, self.directory, self.environment)
