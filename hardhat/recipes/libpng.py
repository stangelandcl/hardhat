from .base import GnuRecipe


class LibPngRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibPngRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '266743a326986c3dbcee9d89b640595f' \
                      '6b16a293fd02b37d8c91348d317b73f9'

        self.name = 'libpng'
        self.version = '1.6.26'
        self.depends = ['zlib']
        self.url = 'http://download.sourceforge.net/$name/' \
                   '$name-$version.tar.xz'
