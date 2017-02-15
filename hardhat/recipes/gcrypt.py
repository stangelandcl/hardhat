from .base import GnuRecipe


class GCryptRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GCryptRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '626aafee84af9d2ce253d2c143dc1c09' \
                      '02dda045780cc241f39970fc60be05bc'

        self.name = 'gcrypt'
        self.version = '1.7.6'
        self.url = 'ftp://ftp.gnupg.org/gcrypt/lib$name/' \
            'lib$name-$version.tar.bz2'

        self.configure_strip_cross_compile()
        self.environment_strip_lto()
