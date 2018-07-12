from .base import GnuRecipe


class LibAssuanRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibAssuanRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '47f96c37b4f2aac289f0bc1bacfa8bd8' \
                      'b4b209a488d3d15e2229cb6cc9b26449'

        self.name = 'libassuan'
        self.version = '2.5.1'
        self.url = 'ftp://ftp.gnupg.org/gcrypt/libassuan/' \
                   'libassuan-$version.tar.bz2'
