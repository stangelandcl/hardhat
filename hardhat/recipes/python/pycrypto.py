from .base import PipBaseRecipe


class PyCryptoRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyCryptoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f2ce1e989b272cfcb677616763e0a2e7' \
                      'ec659effa67a88aa92b3a65528f60a3c'

        self.name = 'pycrypto'
        self.version = '2.6.1'
