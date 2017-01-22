from .base import X11BaseRecipe


class LibXcursorRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXcursorRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9bc6acb21ca14da51bda5bc912c8955b' \
                      'c6e5e433f0ab00c5e8bef842596c33df'

        self.name = 'libXcursor'
        self.version = '1.1.14'
        self.depends = ['libX11', 'libXfixes', 'libXrender', 'xorg-headers']
