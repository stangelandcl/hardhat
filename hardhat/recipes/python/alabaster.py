from .base import PipBaseRecipe


class AlabasterRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AlabasterRecipe, self).__init__(*args, **kwargs)
        self.name = 'alabaster'
        self.version = '0.7.10'
