from .base import GnuRecipe
from .cacert import CACertRecipe


class CurlRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CurlRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f50ebaf43c507fa7cc32be4b8108fa8b' \
                      'bd0f5022e90794388f3c7694a302ff06'

        self.name = 'curl'
        self.version = '7.54.0'
        if self.mingw64:
            self.depends = ['zlib']
        else:
            self.depends = ['cacert', 'openldap', 'openssl', 'zlib']
        self.url = 'https://curl.haxx.se/download/curl-$version.tar.bz2'
        self.configure_args += [
            '--enable-ldap',
            '--enable-ldaps',
            '--with-zlib',
            ]
        if self.mingw64:
            self.configure_args += ['--with-winssl']
            self.environment['CFLAGS'] += ' -DWIN32_LEAN_AND_MEAN'
        else:
            self.configure_args += [
                '--with-ca-bundle=%s' % CACertRecipe.bundle_path(
                    self.prefix_dir),
                '--with-ca-path=%s' % CACertRecipe.certs_path(self.prefix_dir),
                ]
