from .base import PipBaseRecipe


class ZopeDeprecationRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ZopeDeprecationRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7d52e134bbaaa0d72e1e2bc90f0587f1' \
                      'adc116c4bdf15912afaf2f1e8856b224'
        self.pydepends = ['setuptools']
        self.name = 'zope.deprecation'
        self.version = '4.3.0'
