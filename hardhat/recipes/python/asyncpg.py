from .base import PipBaseRecipe


class AsyncPgRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AsyncPgRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '31d5a9d993ce97924d9601bf6a37bb8b' \
                      '542d63bc8716b36238511e5e5915b14c'

        self.name = 'asyncpg'
        self.depends = ['postgres']
        self.version = '0.16.0'
