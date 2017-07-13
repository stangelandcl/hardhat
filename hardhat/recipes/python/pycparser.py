from .base import PipBaseRecipe


class PyCParserRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyCParserRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0aac31e917c24cb3357f5a4d5566f2cc' \
                      '91a19ca41862f6c3c22dc60a629673b6'

        self.name = 'pycparser'
        self.version = '2.17'
