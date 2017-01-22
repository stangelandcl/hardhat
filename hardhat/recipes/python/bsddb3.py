from .base import PipBaseRecipe


class BsdDb3Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(BsdDb3Recipe, self).__init__(*args, **kwargs)

        self.name = 'bsddb3'
        self.version = '6.2.0'
        self.sha256 = '3c24cb287e1dd08be387a2b4d32ae5df' \
                      'eba5ef4e3785878f0030e4d4f608aba9'

        self.environment['LIBS'] = ''
