from .base import PipBaseRecipe


class TornadoRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(TornadoRecipe, self).__init__(*args, **kwargs)

        self.name = 'tornado'
        self.version = '5.1'
