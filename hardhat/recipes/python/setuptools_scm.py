from .base import PipBaseRecipe


class SetupToolsScmRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SetupToolsScmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e163e8a12d2121f77575773cfc2b5988' \
                      '275dc1f1d2541fdf780127c29dbbea9c'
        self.name = 'setuptools_scm'
        self.version = '1.15.7'
        self.pydepends = ['setuptools']
