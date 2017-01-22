from .base import PipBaseRecipe


class ZopeInterfaceRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ZopeInterfaceRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '36762743940a075283e1fb22a2ec9e82' \
                      '31871dace2aa00599511ddc4edf0f8f9'

        self.name = 'zope.interface'
        self.pydepends = ['setuptools']
        self.version = '4.2.0'
