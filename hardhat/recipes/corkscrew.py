from .base import GnuRecipe


class CorkscrewRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CorkscrewRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0d0fcbb41cba4a81c4ab494459472086' \
                      'f377f9edb78a2e2238ed19b58956b0be'

        self.name = 'corkscrew'
        self.version = '2.0'
        self.url = 'http://agroman.net/corkscrew/corkscrew-$version.tar.gz'
