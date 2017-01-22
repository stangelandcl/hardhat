from .base import PipBaseRecipe


class PatsyRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PatsyRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'dc1cc280045b0e6e50c04706fd1e26d2' \
                      'a00ea400aa112f88e8142f88b0b7d3d4'

        self.name = 'patsy'
        self.version = '0.4.1'
