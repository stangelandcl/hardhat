from .base import PipBaseRecipe


class BackportsLzmaRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(BackportsLzmaRecipe, self).__init__(*args, **kwargs)

        self.pythons = ['python2']
        self.name = 'backports.lzma'
        self.version = '0.0.3'
