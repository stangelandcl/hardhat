from .base import PipBaseRecipe


class TornadoRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(TornadoRecipe, self).__init__(*args, **kwargs)

        self.name = 'tornado'
        self.version = '4.3'
        self.sha256 = 'c9c2d32593d16eedf2cec1b6a41893626' \
                      'a2649b40b21ca9c4cac4243bde2efbf'
