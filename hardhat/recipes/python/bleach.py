from .base import PipBaseRecipe


class BleachRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(BleachRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b9522130003e4caedf4f00a39c120a90' \
                      '6dcd4242329c1c8f621f5370203cbc30'

        self.name = 'bleach'
        self.version = '2.0.0'
        self.pydepends = ['html5lib']
