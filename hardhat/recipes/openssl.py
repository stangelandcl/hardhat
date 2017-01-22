from .base import GnuRecipe


class OpenSSLRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpenSSLRecipe, self).__init__(*args, **kwargs)
#        self.sha256 = 'fc436441a2e05752d31b4e46115eb897' \
#                      '09a28aef96d4fe786abe92409b2fd6f5'
#       self.version = '1.1.0c'
        self.sha256 = 'e7aff292be21c259c6af26469c7a9b3b' \
                      'a26e9abaaffd325e3dccc9785256c431'

        self.version = '1.0.2j'
        self.name = 'openssl'

        self.depends = ['zlib']
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
