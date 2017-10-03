from .base import GnuRecipe


class TinyCCRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TinyCCRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '99a73384b8c30808688bf95cecfa4c51' \
                      '1d1dfb72b67b6f365bc2c42c52b3f426'
        self.name = 'tinycc'
        self.version = '2e5751caf120dc4d86f9a727fb56db12202b59cd'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools']
        self.url = 'http://repo.or.cz/tinycc.git/snapshot/$version.tar.gz'
