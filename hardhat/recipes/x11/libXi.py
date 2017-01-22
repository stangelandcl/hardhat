from .base import X11BaseRecipe


class LibXiRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXiRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd8f2fa8d53141c41ff521627df9b2fa9' \
                      'c05f6f142fd9881152bab36549ac27bb'

        self.name = 'libXi'
        self.version = '1.7.8'
        self.depends = ['libXext', 'libX11', 'xorg-headers']
