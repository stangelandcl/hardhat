from .base import PipBaseRecipe


class PyParsingRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyParsingRecipe, self).__init__(*args, **kwargs)

        self.name = 'pyparsing'
        self.version = '2.1.4'
        self.sha256 = 'a9234dea79b50d49b92a994132cd1c84' \
                      'e873f3936db94977a66f0a4159b1797c'
