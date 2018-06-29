import os
from .base import GnuRecipe
from ..version import extension_regex


class LmdbRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LmdbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f3927859882eb608868c8c31586bb7eb' \
                      '84562a40a6bf5cc3e13b6b564641ea28'
        self.name = 'lmdb'
        self.version = '0.9.22'
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
