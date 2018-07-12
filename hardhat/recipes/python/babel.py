from .base import PipBaseRecipe


class BabelRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(BabelRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8cba50f48c529ca3fa18cf81fa9403be' \
                      '176d374ac4d60738b839122dfaaa3d23'

        self.name = 'babel'
        self.version = '2.6.0'
        self.pypi_name = 'Babel'
        self.depends = ['python-pytz']
