from .base import PipBaseRecipe


class ChardetRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ChardetRecipe, self).__init__(*args, **kwargs)
        self.name = 'chardet'
        self.version = '3.0.4'
