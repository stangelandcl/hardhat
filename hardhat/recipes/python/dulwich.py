from .base import PipBaseRecipe


class DulwichRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DulwichRecipe, self).__init__(*args, **kwargs)
        self.name = 'dulwich'
        self.depends = []
        self.version = '0.17.3'
