from .base import PipBaseRecipe


class RsaRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(RsaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '25df4e10c263fb88b5ace923dd84bf9a' \
                      'a7f5019687b5e55382ffcdb8bede9db5'

        self.name = 'rsa'
        self.version = '3.4.2'
        self.pydepends = ['pyasn1']
