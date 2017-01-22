from .base import GnuRecipe


class LibDvdCssRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibDvdCssRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2089375984800df29a4817b37f3123c1' \
                      '706723342d6dab4d0a8b75c25c2c845a'

        self.name = 'libdvdcss'
        self.version = '1.4.0'
        self.url = 'http://download.videolan.org/libdvdcss/$version/' \
                   'libdvdcss-$version.tar.bz2'
