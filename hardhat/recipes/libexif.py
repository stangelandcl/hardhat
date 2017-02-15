from .base import GnuRecipe


class LibExifRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibExifRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '16cdaeb62eb3e6dfab2435f7d7bccd2f' \
                      '37438d21c5218ec4e58efa9157d4d41a'
        self.name = 'libexif'
        self.version = '0.6.21'
        self.url = 'http://downloads.sourceforge.net/libexif/' \
                   'libexif-$version.tar.bz2'
