from .base import GnuRecipe


class NnnRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NnnRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '88dd08d624ae7a61ef749b1e258e4b29' \
                      'ed61ba9fcc5a18813f291ce80efc5e74'
        self.name = 'nnn'
        self.version = '2.2'
        self.version_regex = r'(?P<version>\d+\.\d+\)'
        self.version_url = 'https://github.com/jarun/nnn/releases'
        self.depends = ['autotools', 'ncurses']
        self.url = 'https://github.com/jarun/nnn/archive/v$version.tar.gz'






