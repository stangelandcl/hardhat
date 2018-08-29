from .base import X11BaseRecipe


class LibXfixesRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXfixesRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'de1cd33aff226e08cefd0e6759341c2c' \
                      '8e8c9faf8ce9ac6ec38d43e287b22ad6'

        self.name = 'libXfixes'
        self.version = '5.0.3'
        self.depends = ['libX11', 'xorgproto']
