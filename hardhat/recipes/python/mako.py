from .base import PipBaseRecipe


class MakoRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(MakoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4e02fde57bd4abb5ec400181e4c314f5' \
                      '6ac3e49ba4fb8b0d50bba18cb27d25ae'

        self.pythons = ['python3']
        self.name = 'mako'
        self.version = '1.0.7'
