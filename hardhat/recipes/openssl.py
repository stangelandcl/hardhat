from .base import GnuRecipe
from ..version import Versions


class OpenSSLRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpenSSLRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ec3f5c9714ba0fd45cb4e087301eb133' \
                      '6c317e0d20b575a125050470e8089e4d'

        self.version = '1.0.2o'
        self.name = 'openssl'

        self.depends = ['zlib']
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
