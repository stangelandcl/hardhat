from .base import GnuRecipe
from ..version import extension_regex


class ZstdRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ZstdRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '980b8febb0118e22f6ed70d23b5b3e60' \
                      '0995dbf7489c1f6d6122c1411cdda8d8'

        self.name = 'zstd'
        self.version = '1.1.2'
        self.version_regex = 'v(?P<version>\d+\.\d+\.\d+)' + extension_regex
        self.version_url = 'https://github.com/facebook/zstd/releases'
        self.url = 'https://github.com/facebook/zstd/archive/v$version.tar.gz'

        self.compile_args += ['PREFIX=%s' % self.prefix_dir]
        self.install_args += ['PREFIX=%s' % self.prefix_dir]
        self.environment['CFLAGS'] = \
            self.environment['CFLAGS'].replace('-O2', '-O3')
        self.environment['CXXFLAGS'] = \
            self.environment['CXXFLAGS'].replace('-O2', '-O3')
