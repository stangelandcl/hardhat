from .base import PipBaseRecipe


class ZopeInterfaceRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ZopeInterfaceRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '57c38470d9f57e37afb460c399eb254e' \
                      '7193ac7fb8042bd09bdc001981a9c74c'

        self.name = 'zope.interface'
        self.pydepends = ['setuptools']
        self.version = '4.5.0'
