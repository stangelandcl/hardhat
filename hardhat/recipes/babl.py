from .base import GnuRecipe


class BablRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BablRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4d2bf1345d7214b08762e6d1e23d0038' \
                      '508b806dbf7c4c44386faee434682a07'
        self.name = 'babl'
        self.version = '0.1.54'
        self.depends = ['gobject-introspection']
        self.url = 'http://download.gimp.org/pub/babl/0.1/babl-$version.tar.bz2'
