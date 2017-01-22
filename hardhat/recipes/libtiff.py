from .base import GnuRecipe


class LibTiffRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibTiffRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4d57a50907b510e3049a4bba0d788893' \
                      '0fdfc16ce49f1bf693e5b6247370d68c'
        self.name = 'libtiff'
        self.version = '4.0.6'
        self.url = 'http://download.osgeo.org/libtiff/tiff-$version.tar.gz'
