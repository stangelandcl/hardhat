from .base import GnuRecipe


class MpfrRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MpfrRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '015fde82b3979fbe5f83501986d32833' \
                      '1ba8ddf008c1ff3da3c238f49ca062bc'

        self.name = 'mpfr'
        self.version = '3.1.5'
        self.depends = ['gmp']
        self.url = 'http://www.mpfr.org/mpfr-current/mpfr-$version.tar.xz'
