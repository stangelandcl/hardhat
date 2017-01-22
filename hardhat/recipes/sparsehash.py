from .base import GnuRecipe


class SparseHashRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SparseHashRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '05e986a5c7327796dad742182b2d1080' \
                      '5a8d4f511ad090da0490f146c1ff7a8c'

        self.name = 'sparsehash'
        self.version = '2.0.3'
        self.version_url = 'https://github.com/google/snappy/releases'
        self.url = 'https://github.com/sparsehash/sparsehash/archive/' \
                   'sparsehash-$version.tar.gz'
