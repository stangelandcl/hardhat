from .base import PipBaseRecipe


class WerkzeugRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(WerkzeugRecipe, self).__init__(*args, **kwargs)

        self.name = 'werkzeug'
        self.version = '0.11.9'
        self.pypi_name = 'Werkzeug'
        self.sha256 = '837b71338794634c24713a79c3b9c28' \
                      '7301433f2d18cd0adefcbcf885e60c8a1'
