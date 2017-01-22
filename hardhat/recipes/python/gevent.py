from .base import PipBaseRecipe


class GeventRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(GeventRecipe, self).__init__(*args, **kwargs)

        self.name = 'gevent'
        self.depends = ['c-ares', 'libev']
        self.pydepends = ['greenlet']
        self.version = '1.1.2'
        self.sha256 = 'cb15cf73d69a2eeefed330858f09634e' \
                      '2c50bf46da9f9e7635730fcfb872c02c'

        self.environment['CARES_EMBED']=''
        self.environment['LIBEV_EMBED']=''
