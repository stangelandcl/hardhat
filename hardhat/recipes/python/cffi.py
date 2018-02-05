from .base import PipBaseRecipe


class CffiRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CffiRecipe, self).__init__(*args, **kwargs)
        self.name = 'cffi'
        self.version = '1.11.4'
        self.depends = ['libffi']
        self.pydepends = ['pycparser']
