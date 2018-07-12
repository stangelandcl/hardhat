from .base import PipBaseRecipe


class IdnaRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(IdnaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '684a38a6f903c1d71d6d5fac066b58d7' \
                      '768af4de2b832e426ec79c30daa94a16'
        self.name = 'idna'
        self.version = '2.7'
