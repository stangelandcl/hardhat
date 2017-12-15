from .base import PipBaseRecipe


class DillRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DillRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '97fd758f5fe742d42b11ec8318ecfcff' \
                      '8776bccacbfcec05dfd6276f5d450f73'

        self.pythons = ['python3']
        self.name = 'dill'
        self.version = '0.2.7.1'
