from .base import GnuRecipe
from .cacert import CACertRecipe


class CurlRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CurlRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'de60a4725a3d461c70aa571d7d69c788' \
                      'f1816d9d1a8a2ef05f864ce8f01279df'

        self.name = 'curl'
        self.version = '7.56.0'
        self.depends = ['cacert', 'openldap', 'openssl', 'zlib']
        self.url = 'https://curl.haxx.se/download/curl-$version.tar.bz2'
        self.configure_args += [
            '--enable-ldap',
            '--enable-ldaps',
            '--with-zlib',
            ]

    def configure(self):
        self.configure_args += [
            '--with-ca-bundle=%s' % CACertRecipe.bundle_path(
                self.prefix_dir),
            '--with-ca-path=%s' % CACertRecipe.certs_path(self.prefix_dir),
            ]

        super(CurlRecipe, self).configure()
