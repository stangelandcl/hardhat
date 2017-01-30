from .base import GnuRecipe


class HunspellRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(HunspellRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '512e7d2ee69dad0b35ca011076405e56' \
                      'e0f10963a02d4859dbcc4faf53ca68e2'
        self.name = 'hunspell'
        self.version = '1.6.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'ncurses', 'readline']
        self.url = 'https://github.com/hunspell/hunspell/archive/' \
                   'v$version.tar.gz'
        self.configure_args += ['--with-ui',
                                '--with-readline']
        self.configure_args = [['autoreconf', '-vfi'],
                               self.configure_args]
