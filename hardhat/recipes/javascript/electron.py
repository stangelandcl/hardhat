from .base import NpmBaseRecipe


class ElectronRecipe(NpmBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ElectronRecipe, self).__init__(*args, **kwargs)
        self.name = 'electron'
        self.version = '1.6.15'
