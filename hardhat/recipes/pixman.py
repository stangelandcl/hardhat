from .base import GnuRecipe


class PixmanRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PixmanRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '21b6b249b51c6800dc9553b65106e1e3' \
                      '7d0e25df942c90531d4c3997aa20a88e'

        self.name = 'pixman'
        self.version = '0.34.0'
        self.url = 'http://cairographics.org/releases/$name-$version.tar.gz'
