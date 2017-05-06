from .base import GnuRecipe


class LibArchiveRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibArchiveRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '29ca5bd1624ca5a007aa57e16080262a' \
                      'b4379dbf8797f5c52f7ea74a3b0424e7'

        self.name = 'libarchive'
        self.version = '3.3.1'
        self.depends = ['libxml2', 'lzo', 'nettle']
        self.url = 'http://www.libarchive.org/downloads/' \
                   'libarchive-$version.tar.gz'
