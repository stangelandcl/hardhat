import os
from .base import Mingw64BaseRecipe
from hardhat.version import extension_regex


class Mingw64Lz4Recipe(Mingw64BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Mingw64Lz4Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '0190cacd63022ccb86f44fa5041dc6c3' \
                      '804407ad61550ca21c382827319e7e7e'
        self.name = 'mingw64-lz4'
        self.version = '1.7.5'
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
