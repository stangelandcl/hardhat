from .base import GnuRecipe
from .cacert import CACertRecipe


class CurlRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CurlRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5f6f336921cf5b84de56afbd08dfb70a' \
                      'deef2303751ffb3e570c936c6d656c9c'
        self.name = 'curl'
        self.version = '7.61.0'
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
