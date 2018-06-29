from .base import GnuRecipe
from ..version import extension_regex


class ZstdRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ZstdRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '92e41b6e8dd26bbd46248e8aa1d86f15' \
                      '51bc221a796277ae9362954f26d605a9'
        self.name = 'zstd'
        self.version = '1.3.4'
        self.version_regex = 'v(?P<version>\d+\.\d+\.\d+)' + extension_regex
        self.version_url = 'https://github.com/facebook/zstd/releases'
        self.url = 'https://github.com/facebook/zstd/archive/v$version.tar.gz'

        self.compile_args += ['PREFIX=%s' % self.prefix_dir]
        self.install_args += ['PREFIX=%s' % self.prefix_dir]
        self.environment['CFLAGS'] = \
            self.environment['CFLAGS'].replace('-O2', '-O3')
        self.environment['CXXFLAGS'] = \
            self.environment['CXXFLAGS'].replace('-O2', '-O3')
