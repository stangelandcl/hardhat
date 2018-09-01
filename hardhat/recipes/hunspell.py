from .base import GnuRecipe


class HunspellRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(HunspellRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3cd9ceb062fe5814f668e4f22b2fa6e3' \
                      'ba0b339b921739541ce180cac4d6f4c4'

        self.name = 'hunspell'
        self.version = '1.6.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'ncurses', 'readline']
        self.url = 'https://github.com/hunspell/hunspell/archive/' \
                   'v$version.tar.gz'
        self.configure_args += ['--with-ui',
                                '--with-readline']
        self.configure_args = [['autoreconf', '-vfi'],
                               self.configure_args]
