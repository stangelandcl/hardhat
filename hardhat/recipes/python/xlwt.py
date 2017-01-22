from .base import PipBaseRecipe


class XlwtRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(XlwtRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '505669c1eb6a60823fd3e2e723b60eea' \
                      '95f2c56254113bf163091ed2bedb4ac9'

        self.name = 'xlwt'
        self.version = '1.2.0'
