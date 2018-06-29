from .base import GnuRecipe


class OpenLdapRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpenLdapRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9a90dcb86b99ae790ccab93b7585a31f' \
                      'bcbeec8c94bf0f7ab0ca0a87ea0c4b2d'
        self.name = 'openldap'
        self.version = '2.4.46'
        self.depends = ['cyrus-sasl', 'icu', 'libtool', 'openssl']
        self.url = 'http://www.openldap.org/software/download/OpenLDAP/' \
                   'openldap-release/openldap-$version.tgz'
        self.version_url = 'http://www.openldap.org/software/download/' \
                           'OpenLDAP/openldap-release/'
        self.version_regex = r'openldap-(?P<version>\d+\.\d+\.\d+)\.tgz'
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
