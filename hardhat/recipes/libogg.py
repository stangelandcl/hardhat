from .base import GnuRecipe


class LibOggRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibOggRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4f3fc6178a533d392064f14776b23c39' \
                      '7ed4b9f48f5de297aba73b643f955c08'
        self.name = 'libogg'
        self.version = '1.3.3'
        self.url = 'http://downloads.xiph.org/releases/ogg/' \
                   'libogg-$version.tar.xz'
