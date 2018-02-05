from .base import PipBaseRecipe


class SetupToolsScmRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SetupToolsScmRecipe, self).__init__(*args, **kwargs)
        self.name = 'setuptools_scm'
        self.version = '1.15.7'
        self.pydepends = ['setuptools']
