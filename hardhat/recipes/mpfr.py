from .base import GnuRecipe


class MpfrRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MpfrRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'cf4f4b2d80abb79e820e78c8077b6725' \
                      'bbbb4e8f41896783c899087be0e94068'
        
        self.name = 'mpfr'
        self.version = '3.1.6'
        self.depends = ['gmp']
        self.url = 'http://www.mpfr.org/mpfr-$version/mpfr-$version.tar.xz'
