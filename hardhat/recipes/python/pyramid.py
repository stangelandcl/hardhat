from .base import PipBaseRecipe


class PyramidRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyramidRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1218140ea016dcb63b962d44e43c6d26' \
                      'e448e6c2a49133dc52d01f01fbb2d5c3'
        self.name = 'pyramid'
        self.version = '1.8.3'
        self.pydepends = ['hupper',
                          'PasteDeploy',
                          'repoze.lru',
                          'setuptools',
                          'translationstring',
                          'venusian',
                          'WebOb',
                          'zope.deprecation',
                          'zope.interface']

