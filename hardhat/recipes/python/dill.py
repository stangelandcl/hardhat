from .base import PipBaseRecipe


class DillRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DillRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ffa40ac8a000af69d94090f68bbc434e' \
                      'f98d762a882ad72fed5c4b3bb0e1935b'

        self.pythons = ['python3']
        self.name = 'dill'
        self.version = '0.2.8'
