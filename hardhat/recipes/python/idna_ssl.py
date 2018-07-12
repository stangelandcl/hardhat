from .base import PipBaseRecipe


class IdnaSslRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(IdnaSslRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a933e3bb13da54383f9e8f35dc4f9cb9' \
                      'eb9b3b78c6b36f311254d6d0d92c6c7c'
        self.name = 'idna-ssl'
        self.version = '1.1.0'
