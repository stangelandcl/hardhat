from .base import PipBaseRecipe


class PygmentsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PygmentsRecipe, self).__init__(*args, **kwargs)

        self.name = 'pygments'
        self.version = '2.1.3'
        self.pypi_name = 'Pygments'
        self.sha256 = '88e4c8a91b2af5962bfa5ea2447ec6dd' \
                      '357018e86e94c7d14bd8cacbc5b55d81'
