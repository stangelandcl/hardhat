from .base import PipBaseRecipe


class PyCParserRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyCParserRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '99a8ca03e29851d96616ad0404b4aad7' \
                      'd9ee16f25c9f9708a11faf2810f7b226'

        self.name = 'pycparser'
        self.version = '2.18'
