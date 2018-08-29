from .base import X11BaseRecipe


class LibXineramaRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXineramaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7a45699f1773095a3f821e491cbd5e10' \
                      'c887c5a5fce5d8d3fced15c2ff7698e2'

        self.name = 'libXinerama'
        self.version = '1.1.3'
        self.depends = ['libXext', 'libX11', 'xorgproto']
