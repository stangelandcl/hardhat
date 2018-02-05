from .base import PipBaseRecipe


class IdnaRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(IdnaRecipe, self).__init__(*args, **kwargs)
        self.name = 'idna'
        self.version = '2.6'
