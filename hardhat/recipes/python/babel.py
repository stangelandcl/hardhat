from .base import PipBaseRecipe


class BabelRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(BabelRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8c98f5e5f8f5f088571f2c6bd88d530e' \
                      '331cbbcb95a7311a0db69d3dca7ec563'

        self.name = 'babel'
        self.version = '2.4.0'
        self.pypi_name = 'Babel'
        self.depends = ['python-pytz']
