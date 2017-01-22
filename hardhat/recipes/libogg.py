from .base import GnuRecipe


class LibOggRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibOggRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3f687ccdd5ac8b52d76328fbbfebc70c' \
                      '459a40ea891dbf3dccb74a210826e79b'

        self.name = 'libogg'
        self.version = '1.3.2'
        self.url = 'http://downloads.xiph.org/releases/ogg/' \
                   'libogg-$version.tar.xz'
