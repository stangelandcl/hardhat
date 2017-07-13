from .base import PipBaseRecipe


class AlabasterRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AlabasterRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '37cdcb9e9954ed60912ebc1ca12a9d12' \
                      '178c26637abdf124e3cde2341c257fe0'
        self.name = 'alabaster'
        self.version = '0.7.10'
