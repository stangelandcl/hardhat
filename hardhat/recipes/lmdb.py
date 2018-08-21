import os
from .base import GnuRecipe
from ..version import extension_regex
from ..util import patch


class LmdbRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LmdbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '871d754a707c9968106dd7c7095dcd83' \
                      '18938bb530f8fb020fd175bbd137584d'
        self.name = 'lmdb'
        self.version = '5fced32bbebe95a125b11474f9190e63c47e82b9'
        self.version_regex = 'LMDB_(?P<version>\d+\.\d+\.\d+)' \
            + extension_regex
        self.url = self.github_commit('stangelandcl')

        self.compile_args += [
            'XCFLAGS="-DMDB_MAXKEYSIZE=1800"',
            'OPT="%s"' % self.environment['OPT'],
            ]

        self.install_args += [
            'prefix=""',
            'DESTDIR=%s' % (self.prefix_dir)]

    def extract(self):
        super(LmdbRecipe, self).extract()
        self.directory = os.path.join(self.directory, 'libraries', 'liblmdb')

    def configure(self):
        pass

#    def patch(self):
#        src = 'env->me_psize = env->me_os_psize;'
#        dst = 'env->me_psize = 65536;'
#        patch(os.path.join(self.directory, 'mdb.c'), src, dst)
