from .base import PipBaseRecipe


class PyParsingRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyParsingRecipe, self).__init__(*args, **kwargs)

        self.name = 'pyparsing'
        self.version = '2.2.0'
