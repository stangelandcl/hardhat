from .base import GnuRecipe
from .cacert import CACertRecipe


class CurlRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CurlRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b5920ffd6a8c95585fb95070e0ced383' \
                      '22790cb335c39d0dab852d12e157b5a0'

        self.name = 'curl'
        self.version = '7.59.0'
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
