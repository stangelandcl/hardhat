from .base import PipBaseRecipe


class PyCParserRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyCParserRecipe, self).__init__(*args, **kwargs)

        self.name = 'pycparser'
        self.version = '2.17'
