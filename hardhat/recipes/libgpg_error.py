from .base import GnuRecipe


class LibGpgErrorRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibGpgErrorRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4c4bcbc90116932e3acd37b37812d865' \
                      '3b1b189c1904985898e860af818aee69'

        self.name = 'libgpg-error'
        self.version = '1.26'
        self.url = 'https://www.gnupg.org/ftp/gcrypt/libgpg-error/' \
            'libgpg-error-%s.tar.bz2' % (self.version)

        self.configure_strip_cross_compile()
