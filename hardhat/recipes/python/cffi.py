from .base import PipBaseRecipe


class CffiRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CffiRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'df9083a992b17a28cd4251a3f5c879e0' \
                      '198bb26c9e808c4647e0a18739f1d11d'

        self.name = 'cffi'
        self.version = '1.11.4'
        self.depends = ['libffi']
        self.pydepends = ['pycparser']
