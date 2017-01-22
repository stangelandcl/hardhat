from .base import PipBaseRecipe


class TabulateRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(TabulateRecipe, self).__init__(*args, **kwargs)

        self.name = 'tabulate'
        self.version = '0.7.5'
        self.sha256 = '9071aacbd97a9a915096c1aaf0dc684a' \
                      'c2672904cd876db5904085d6dac9810e'
