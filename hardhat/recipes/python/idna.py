from .base import PipBaseRecipe


class IdnaRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(IdnaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2c6a5de3089009e3da7c5dde64a141db' \
                      'c8551d5b7f6cf4ed7c2568d0cc520a8f'

        self.name = 'idna'
        self.version = '2.6'
