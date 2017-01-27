from .base import PipBaseRecipe


class OleFileRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(OleFileRecipe, self).__init__(*args, **kwargs)

        self.name = 'olefile'
        self.version = '0.44'
        self.sha256 = '61f2ca0cd0aa77279eb943c07f607438' \
                      'edf374096b66332fae1ee64a6f0f73ad'
