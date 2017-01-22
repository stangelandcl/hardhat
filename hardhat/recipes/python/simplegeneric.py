from .base import PipBaseRecipe


class SimpleGenericRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SimpleGenericRecipe, self).__init__(*args, **kwargs)

        self.name = 'simplegeneric'
        self.version = '0.8.1'
        self.sha256 = 'dc972e06094b9af5b855b3df4a646395' \
                      'e43d1c9d0d39ed345b7393560d0b9173'
