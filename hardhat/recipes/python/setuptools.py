from .base import PipBaseRecipe


class SetupToolsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SetupToolsRecipe, self).__init__(*args, **kwargs)
        self.name = 'setuptools'
        self.version = '40.2.0'
        self.pydepends = ['appdirs']
