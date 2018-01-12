from .base import GnuRecipe


class PgBouncerRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PgBouncerRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fa8bde2a2d2c8c80d53a859f8e48bc67' \
                      '13cf127e31c77d8f787bbc1d673e8dc8'

        self.name = 'pgbouncer'
        self.version = '1.8.1'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://pgbouncer.github.io/downloads/'
        self.depends = ['libevent', 'openssl']
        self.url = 'https://pgbouncer.github.io/downloads/files/$version/' \
                   'pgbouncer-$version.tar.gz'
#        self.configure_strip_cross_compile()
