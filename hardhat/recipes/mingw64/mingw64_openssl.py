from .base import Mingw64BaseRecipe
from hardhat.version import Versions


class Mingw64OpenSSLRecipe(Mingw64BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Mingw64OpenSSLRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6b3977c61f2aedf0f96367dcfb5c6e57' \
                      '8cf37e7b8d913b4ecb6643c3cb88d8c0'

        self.version = '1.0.2k'
        self.name = 'mingw64-openssl'

        self.depends = ['mingw64-zlib']
        self.version_regex = r'openssl-(?P<version>1\.0\.\d+\w+)'
        self.version_url = 'https://www.openssl.org/source/'
        self.url = 'https://www.openssl.org/source/openssl-$version.tar.gz'
        self.cpu_count = 1  # multi-core not supported by openssl
        self.configure_args = self.shell_args + [
            './config',
            '--prefix=%s' % (self.prefix_dir),
            '--libdir=lib',
            'shared',
            'zlib-dynamic'
            ]
        self.install_args += ['MANDIR=%s/share/man MANSUFFIX=ssl'
                              % (self.prefix_dir)]

        self.compile_args = ['make']

    def get_version_always(self):
        return Versions.scrape_page(self.version_url, self.version_regex)
