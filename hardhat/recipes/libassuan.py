from .base import GnuRecipe


class LibAssuanRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibAssuanRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '22843a3bdb256f59be49842abf24da76' \
                      '700354293a066d82ade8134bb5aa2b71'

        self.name = 'libassuan'
        self.version = '2.4.3'
        self.url = 'ftp://ftp.gnupg.org/gcrypt/libassuan/' \
                   'libassuan-$version.tar.bz2'
