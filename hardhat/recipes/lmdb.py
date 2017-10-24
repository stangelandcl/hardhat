import os
from .base import GnuRecipe
from ..version import extension_regex


class LmdbRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LmdbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '108532fb94c6f227558d45be3f3347b5' \
                      '2539f0f58290a7bb31ec06c462d05326'

        self.name = 'lmdb'
        self.version = '0.9.19'
        self.version_regex = 'LMDB_(?P<version>\d+\.\d+\.\d+)' \
            + extension_regex
        self.version_url = 'https://github.com/LMDB/lmdb/releases'
        self.url = 'https://github.com/LMDB/lmdb/archive/LMDB_$version.tar.gz'

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
