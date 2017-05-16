from .base import PipBaseRecipe


class ZopeDeprecationRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ZopeDeprecationRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ff32c5bb5388b77b22c83ed1f1aa01cd' \
                      'bb076d9f2cfa2b825450ce9e2ecfd738'
                
        self.name = 'zope.deprecation'
        self.version = '4.2.0'
