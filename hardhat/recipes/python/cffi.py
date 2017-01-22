from .base import PipBaseRecipe


class CffiRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CffiRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '563e0bd53fda03c151573217b3a49b3a' \
                      'bad8813de9dd0632e10090f6190fdaf8'

        self.name = 'cffi'
        self.version = '1.9.1'
        self.pydepends = ['pycparser']
