from .base import PipBaseRecipe


class OleFileRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(OleFileRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2b6575f5290de8ab1086f8c5490591f7' \
                      'e0885af682c7c1793bdaf6e64078d385'
        self.name = 'olefile'
        self.version = '0.45.1'
