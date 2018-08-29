from .base import X11BaseRecipe


class LibXFontRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXFontRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '02945ea68da447102f3e6c2b896c1d20' \
                      '61fd115de99404facc2aca3ad7010d71'

        self.name = 'libXfont'
        self.version = '1.5.2'
        self.depends = ['freetype', 'libfontenc', 'xorgproto']
