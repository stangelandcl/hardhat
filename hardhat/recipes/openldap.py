from .base import GnuRecipe


class OpenLdapRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpenLdapRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd7de6bf3c67009c95525dde3a0212cc1' \
                      '10d0a70b92af2af8e3ee800e81b88400'

        self.name = 'openldap'
        self.version = '2.4.44'
        self.depends = ['cyrus-sasl', 'icu', 'openssl']
        self.url = 'ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/' \
                   'openldap-$version.tgz'
        self.configure_args += ['--enable-dynamic',
                                '--disable-debug',
                                '--with-tls=openssl',
                                '--with-cyrus-sasl',
                                '--enable-crypt',
                                '--enable-spasswd',
                                '--enable-slapd',
                                '--enable-modules',
                                '--enable-backends=mod',
                                '--disable-ndb',
                                '--disable-sql',
                                '--disable-shell',
                                '--disable-bdb',
                                '--disable-hdb',
                                '--disable-perl',
                                '--enable-overlays=mod']
        self.configure_strip_cross_compile()

    def compile(self):
        self.compile_args = ['make', 'depend']
        super(OpenLdapRecipe, self).compile()

        self.compile_args = ['make']
        super(OpenLdapRecipe, self).compile()
