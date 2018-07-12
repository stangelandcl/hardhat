from .base import PipBaseRecipe


class WerkzeugRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(WerkzeugRecipe, self).__init__(*args, **kwargs)

        self.name = 'werkzeug'
        self.version = '0.14.1'
        self.pypi_name = 'Werkzeug'
