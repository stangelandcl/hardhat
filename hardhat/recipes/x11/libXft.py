from .base import X11BaseRecipe


class LibXftRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXftRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f5a3c824761df351ca91827ac2210909' \
                      '43ef28b248573486050de89f4bfcdc4c'

        self.name = 'libXft'
        self.version = '2.3.2'
        self.depends = ['fontconfig', 'freetype', 'libXrender']
