from .base import PipBaseRecipe


class CffiRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CffiRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e90f17980e6ab0f3c2f3730e56d1fe9b' \
                      'cba1891eeea58966e89d352492cc74f4'

        self.name = 'cffi'
        self.version = '1.11.5'
        self.depends = ['libffi']
        self.pydepends = ['pycparser']
