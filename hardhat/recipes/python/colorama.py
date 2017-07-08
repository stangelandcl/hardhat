from .base import PipBaseRecipe


class ColoramaRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ColoramaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e043c8d32527607223652021ff648fbb' \
                      '394d5e19cba9f1a698670b338c9d782b'

        self.name = 'colorama'
        self.version = '0.3.7'
