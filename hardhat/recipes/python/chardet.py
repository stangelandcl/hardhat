from .base import PipBaseRecipe


class ChardetRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ChardetRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '84ab92ed1c4d4f16916e05906b6b75a6' \
                      'c0fb5db821cc65e70cbd64a3e2a5eaae'
        self.name = 'chardet'
        self.version = '3.0.4'
