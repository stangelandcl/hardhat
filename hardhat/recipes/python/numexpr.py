from .base import PipBaseRecipe


class NumExprRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(NumExprRecipe, self).__init__(*args, **kwargs)

        self.name = 'numexpr'
        self.version = '2.6.0'
        self.sha256 = '4f31d38cbe24a4780f760761eaf13600' \
                      '959d0a6a72ad8f0946794128e853d144'
