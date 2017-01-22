from .base import X11BaseRecipe


class LibXvMCRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXvMCRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0703d7dff6ffc184f1735ca5d4eb9dbb' \
                      '402b522e08e008f2f96aee16c40a5756'

        self.name = 'libXvMC'
        self.version = '1.0.9'
        self.depends = ['libX11', 'libXext', 'libXv']
