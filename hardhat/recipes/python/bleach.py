from .base import PipBaseRecipe


class BleachRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(BleachRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '978e758599b54cd3caa2e160d7410287' \
                      '9b230ea8dc93871d0783721eef58bc65'

        self.name = 'bleach'
        self.version = '1.5.0'
        self.pydepends = ['html5lib']
