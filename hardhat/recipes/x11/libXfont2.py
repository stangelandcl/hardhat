from .base import X11BaseRecipe


class LibXFont2Recipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXFont2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e9fbbb475ddd171b3a6a54b989cbade1' \
                      'f6f874fc35d505ebc5be426bc6e4db7e'
        self.name = 'libXfont2'
        self.version = '2.0.1'
        self.depends = ['freetype', 'libfontenc', 'xorgproto']
