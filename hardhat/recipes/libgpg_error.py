from .base import GnuRecipe


class LibGpgErrorRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibGpgErrorRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '40d0a823c9329478063903192a1f8249' \
                      '6083b277265904878f4bc09e0db7a4ef'
                
        self.name = 'libgpg-error'
        self.version = '1.31'
        self.url = 'https://www.gnupg.org/ftp/gcrypt/libgpg-error/' \
            'libgpg-error-%s.tar.bz2' % (self.version)

        self.configure_strip_cross_compile()
