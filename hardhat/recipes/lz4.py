import os
from .base import GnuRecipe
from ..version import extension_regex


class Lz4Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Lz4Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '0963fbe9ee90acd1d15e9f09e826eaaf' \
                      '8ea0312e854803caf2db0a6dd40f4464'
        self.name = 'lz4'
        self.version = '1.8.2'
        self.version_regex = r'v(?P<version>\d+\.\d+\.\d+)' + extension_regex
        self.version_url = 'https://github.com/lz4/lz4/releases'
        self.url = 'https://github.com/Cyan4973/lz4/archive/v$version.tar.gz'
        self.filename = os.path.join(
            self.tarball_dir,
            '%s-%s.tar.gz' % (self.name, self.version))

        self.compile_args += ['lib', 'lz4']
        self.install_args += ['PREFIX=%s' % (self.prefix_dir)]

    def configure(self):
        pass
