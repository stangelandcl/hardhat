import os
from .base import GnuRecipe
from ..version import extension_regex
from ..util import patch


class LmdbRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LmdbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '655b4408fa826866df9449c076ba72c8' \
                      '80a2ce072d3668f069e9086fd729b435'
        self.name = 'lmdb'
        self.version = '6169c5e083cc61a8c13f95d274ce9051add07ea7'
        self.version_regex = 'LMDB_(?P<version>\d+\.\d+\.\d+)' \
            + extension_regex
        self.url = self.github_commit('stangelandcl')

        self.compile_args += [
            'XCFLAGS="-DMDB_MAXKEYSIZE=1800"',
#'OPT="-O0 -ggdb3 -DMDB_DEBUG=1"'
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
#        src = 'static txnid_t mdb_debug_start;'
#        dst = 'static txnid_t mdb_debug_start=1;'
#        patch(os.path.join(self.directory, 'mdb.c'), src, dst)
