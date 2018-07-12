from .base import PipBaseRecipe


class AsyncPgRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AsyncPgRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '10efb357cf879f0e7e3ea4ea852b0b52' \
                      '877f208d988aeb626296092d2601e3cd'

        self.name = 'asyncpg'
        self.depends = ['postgres']
        self.version = '0.17.0'
