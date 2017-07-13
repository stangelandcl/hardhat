from .base import PipBaseRecipe


class PyParsingRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyParsingRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0832bcf47acd283788593e7a0f542407' \
                      'bd9550a55a8a8435214a1960e04bcb04'
        self.name = 'pyparsing'
        self.version = '2.2.0'
