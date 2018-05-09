from .base import PipBaseRecipe


class TwistedRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(TwistedRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a4cc164a781859c74de47f17f0e85f4b' \
                      'ce8a3321a9d0892c015c8f80c4158ad9'

        self.pythons = ['python3']
        self.pydepends = ['Automat',
                          'constantly',
                          'hyperlink',
                          'incremental',
                          'zope.interface']
        self.name = 'twisted'
        self.version = '18.4.0'
