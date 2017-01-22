from .base import GnuRecipe


class GCryptRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GCryptRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f49ebc5842d455ae7019def33eb5a014' \
                      'a0f07a2a8353dc3aa50a76fd1dafa924'

        self.name = 'gcrypt'
        self.version = '1.6.5'
        self.url = 'ftp://ftp.gnupg.org/gcrypt/libgcrypt/' \
            'libgcrypt-%s.tar.bz2' % (self.version)

        self.configure_strip_cross_compile()
