from .base import X11BaseRecipe


class LibXauRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXauRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fdd477320aeb5cdd67272838722d6b7d' \
                      '544887dfe7de46e1e7cc0c27c2bea4f2'

        self.name = 'libXau'
        self.version = '1.0.8'
        self.depends = ['xorg-headers']
