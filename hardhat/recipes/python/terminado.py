from .base import PipBaseRecipe


class TerminadoRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(TerminadoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2c0ba1f624067dccaaead7d2247cfe02' \
                      '9806355cef124dc2ccb53c83229f0126'

        self.name = 'terminado'
        self.version = '0.6'
