from .base import PipBaseRecipe


class PipRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PipRecipe, self).__init__(*args, **kwargs)

        self.name = 'pip'
        self.version = '18.0'
