from .base import PipBaseRecipe


class BabelRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(BabelRecipe, self).__init__(*args, **kwargs)

        self.name = 'babel'
        self.version = '2.4.0'
        self.pypi_name = 'Babel'
        self.depends = ['python-pytz']
