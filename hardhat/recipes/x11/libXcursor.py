from .base import X11BaseRecipe


class LibXcursorRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXcursorRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '294e670dd37cd23995e69aae626629d4' \
                      'a2dfe5708851bbc13d032401b7a3df6b'
        self.name = 'libXcursor'
        self.version = '1.1.15'
        self.depends = ['libX11', 'libXfixes', 'libXrender', 'xorg-headers']
