from .base import GnuRecipe


class FopRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FopRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e5af1d81df8f9fab8aa473e6a1c1407c' \
                      '1bf1c3d327df9b04c3861e8247e8b998'

        self.name = 'fop'
        self.version = '2.1'
        self.url = 'https://archive.apache.org/dist/xmlgraphics/fop/source/' \
                   'fop-$version-src.tar.gz'
