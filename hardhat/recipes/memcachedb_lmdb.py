from .base import GnuRecipe


class MemcachedbLmdbRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MemcachedbLmdbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b5dec6f42660c49df68d17cd86b09daf' \
                      '674cf2c574a036f08287fea93f2c17c9'

        self.name = 'memcachedb-lmdb'
        self.description = 'client-server key value database in C++'
        self.version = '20a1c0b75081630706b552f856ea300cfeb8f801'
        self.url = self.github_commit('LMDB', 'memcachedb')
        self.depends = ['libevent', 'lmdb']
        self.configure_args += ['--enable-threads']
