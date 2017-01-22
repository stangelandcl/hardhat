from .base import GnuRecipe


class LibCpuIdRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibCpuIdRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9ad4d85d7a1151b542e1d032db21e72f' \
                      '1530430c83f1428f80bf07ac6239b24d'

        self.name = 'libcpuid'
        self.version = '0.4.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/anrieff/libcpuid/releases'
        self.depends = ['autotools', 'pcre', 'pkgconfig', 'xz', 'zlib']
        self.url = 'https://github.com/anrieff/libcpuid/releases/' \
                   'download/v$version/libcpuid-$version.tar.gz'
