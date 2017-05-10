from .base import PipBaseRecipe


class CffiRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CffiRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b3b02911eb1f6ada203b0763ba924234' \
                      '629b51586f72a21faacc638269f4ced5'

        self.name = 'cffi'
        self.version = '1.10.0'
        self.pydepends = ['pycparser']
