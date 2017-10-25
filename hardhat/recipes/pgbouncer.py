from .base import GnuRecipe


class PgBouncerRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PgBouncerRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'de36b318fe4a2f20a5f60d1c5ea62c1c' \
                      'a331f6813d2c484866ecb59265a160ba'
        self.name = 'pgbouncer'
        self.version = '1.7.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://pgbouncer.github.io/downloads/'
        self.depends = ['libevent']
        self.url = 'https://pgbouncer.github.io/downloads/files/$version/' \
                   'pgbouncer-$version.tar.gz'
        self.configure_strip_cross_compile()
