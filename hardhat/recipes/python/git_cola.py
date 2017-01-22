from .base import SetupPyRecipe


class GitColaRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(GitColaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '41fbd774f43b8d5a5c874e2a6f28a447' \
                      '043ddd40c691f10dfa68d533bed8180a'

        self.name = 'git-cola'
        self.version = '2.9.1'
        self.url = 'https://github.com/git-cola/git-cola/archive/' \
                   'v$version.tar.gz'
