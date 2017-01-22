from .base import GnuRecipe


class ImLib2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ImLib2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '7d2864972801823ce44ca8d5584a67a8' \
                      '8f0e54e2bf47fa8cf4a514317b4f0021'

        self.name = 'imlib2'
        self.version = '1.4.9'
        self.depends = ['giflib',
                        'libpng', 'libjpeg-turbo', 'libtiff',
                        'xorg-libs']
        self.url = 'http://sourceforge.net/projects/enlightenment/files/' \
                   'imlib2-src/$version/imlib2-$version.tar.bz2'
