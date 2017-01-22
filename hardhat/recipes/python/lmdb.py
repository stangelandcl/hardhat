from .base import PipBaseRecipe


class LmdbRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LmdbRecipe, self).__init__(*args, **kwargs)

        self.name = 'lmdb'
        self.version = '0.89'
        self.depends = ['lmdb']
        self.sha256 = '650336607e5644ad7c6c4f995faaac03' \
                      '49b409a30cac765a1d0ec899fd20d76d'

        self.environment['LMDB_FORCE_SYSTEM'] = '1'
#       If you want to force the use of CFFI instead of the C API
#        self.environment['LMDB_FORCE_CFFI'] = '1'
