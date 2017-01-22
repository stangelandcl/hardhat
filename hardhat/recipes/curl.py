from .base import GnuRecipe
from .cacert import CACertRecipe


class CurlRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CurlRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd16185a767cb2c1ba3d5b9096ec54e5e' \
                      'c198b213f45864a38b3bda4bbf87389b'

        self.name = 'curl'
        self.version = '7.52.1'
        self.depends = ['cacert', 'openldap', 'openssl']
        self.url = 'https://curl.haxx.se/download/curl-$version.tar.bz2'
        self.configure_args += [
            '--with-ca-bundle=%s' % CACertRecipe.bundle_path(self.prefix_dir),
            '--with-ca-path=%s' % CACertRecipe.certs_path(self.prefix_dir),
            '--enable-ldap',
            '--enable-ldaps'
            ]
