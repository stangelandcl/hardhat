from .base import PipBaseRecipe


class SnowballstemmerRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SnowballstemmerRecipe, self).__init__(*args, **kwargs)

        self.name = 'snowballstemmer'
        self.version = '1.2.1'
        self.sha256 = '919f26a68b2c17a7634da993d91339e2' \
                      '88964f93c274f1343e3bbbe2096e1128'
