from .base import GnuRecipe


class MtDevRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MtDevRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6677d5708a7948840de734d8b4675d59' \
                      '80d4561171c5a8e89e54adf7a13eba7f'

        self.name = 'mtdev'
        self.version = '1.1.5'
        self.url = 'http://bitmath.org/code/mtdev/mtdev-$version.tar.bz2'
