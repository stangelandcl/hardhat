from .base import PipBaseRecipe


class SetupToolsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SetupToolsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b2757ddac2c41173140b111e246d2007' \
                      '68f6dd314110e1e40661d0ecf9b4d6a6'

        self.name = 'setuptools'
        self.version = '25.2.0'
