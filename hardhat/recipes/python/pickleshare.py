from .base import PipBaseRecipe


class PickleShareRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PickleShareRecipe, self).__init__(*args, **kwargs)

        self.name = 'pickleshare'
        self.version = '0.7.2'
        self.sha256 = '92ee3b0e21632542ecc9a0a245e69a12' \
                      '6f62e5114081bdb0d32e0edd10410033'
