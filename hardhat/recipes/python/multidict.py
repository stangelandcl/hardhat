from .base import PipBaseRecipe


class MultiDictRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(MultiDictRecipe, self).__init__(*args, **kwargs)

        self.name = 'multidict'
        self.version = '1.2.2'
        self.sha256 = '2fc5fab0dd14d4b8193bfc003b33aa14' \
                      'e0d0cbc97d51ba58aa5fd52b1cb9a6a3'
