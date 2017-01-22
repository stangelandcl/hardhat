from .base import X11BaseRecipe


class LibXrenderRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXrenderRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c06d5979f86e64cabbde57c223938db0' \
                      'b939dff49fdb5a793a1d3d0396650949'

        self.name = 'libXrender'
        self.version = '0.9.10'
        self.depends = ['libX11', 'xorg-headers']
