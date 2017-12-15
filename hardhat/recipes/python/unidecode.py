from .base import PipBaseRecipe


class UnidecodeRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(UnidecodeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '280a6ab88e1f2eb5af79edff450021a0' \
                      'd3f0448952847cd79677e55e58bad051'
        self.name = 'unidecode'
        self.version = '0.04.21'
