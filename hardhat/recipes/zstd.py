from .base import GnuRecipe
from ..version import extension_regex


class ZstdRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ZstdRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd6e1559e4cdb7c4226767d4ddc990bff' \
                      '5f9aab77085ff0d0490c828b025e2eea'

        self.name = 'zstd'
        self.version = '1.3.5'
        self.version_regex = 'v(?P<version>\d+\.\d+\.\d+)' + extension_regex
        self.version_url = 'https://github.com/facebook/zstd/releases'
        self.url = 'https://github.com/facebook/zstd/archive/v$version.tar.gz'

        self.compile_args += ['PREFIX=%s' % self.prefix_dir]
        self.install_args += ['PREFIX=%s' % self.prefix_dir]
        self.environment['CFLAGS'] = \
            self.environment['CFLAGS'].replace('-O2', '-O3')
        self.environment['CXXFLAGS'] = \
            self.environment['CXXFLAGS'].replace('-O2', '-O3')
