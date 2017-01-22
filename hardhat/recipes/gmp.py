from .base import GnuRecipe


class GmpRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GmpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5275bb04f4863a13516b2f39392ac5e2' \
                      '72f5e1bb8057b18aec1c9b79d73d8fb2'

        self.name = 'gmp'
        self.version = '6.1.2'
        self.url = 'https://gmplib.org/download/gmp/' \
            'gmp-%s.tar.bz2' % (self.version)

        self.configure_args += ['--enable-cxx']
