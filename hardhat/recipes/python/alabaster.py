from .base import PipBaseRecipe


class AlabasterRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AlabasterRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '47afd43b08a4ecaa45e3496e139a193c' \
                      'e364571e7e10c6a87ca1a4c57eb7ea08'

        self.name = 'alabaster'
        self.version = '0.7.9'
