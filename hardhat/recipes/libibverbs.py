from .base import GnuRecipe


class LibIbverbsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibIbverbsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'cb91baffc5bab7a06e6f6f0eee4d7fc6' \
                      '145cbcc40cafd0b3f495354d9bec356c'

        self.name = 'libibverbs'
        self.version = '1.1.4-1.24.gb89d4d7'
        self.url = 'https://www.openfabrics.org/downloads/libibverbs/' \
                   'libibverbs-$version.tar.gz'
