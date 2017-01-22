from .base import GnuRecipe


class LibAssuanRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibAssuanRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'bb06dc81380b74bf1b64d5849be5c040' \
                      '9a336f3b4c45f20ac688e86d1b5bcb20'

        self.name = 'libassuan'
        self.version = '2.4.2'
        self.url = 'ftp://ftp.gnupg.org/gcrypt/libassuan/' \
                   'libassuan-$version.tar.bz2'
