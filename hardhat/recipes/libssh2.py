from .base import GnuRecipe


class LibSsh2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibSsh2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '39f34e2f6835f4b992cafe8625073a88' \
                      'e5a28ba78f83e8099610a7b3af4676d4'

        self.name = 'libssh2'
        self.version = '1.8.0'
        self.url = 'https://www.libssh2.org/download/libssh2-$version.tar.gz'
        self.depends = ['openssl']
