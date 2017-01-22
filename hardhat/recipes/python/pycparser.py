from .base import PipBaseRecipe


class PyCParserRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyCParserRecipe, self).__init__(*args, **kwargs)

        self.name = 'pycparser'
        self.version = '2.14'
        self.sha256 = '7959b4a74abdc27b312fed1c21e6caf' \
                      '9309ce0b29ea86b591fd2e99ecdf27f73'
