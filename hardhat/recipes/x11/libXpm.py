from .base import X11BaseRecipe


class LibXpmRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXpmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fd6a6de3da48de8d1bb738ab6be4ad67' \
                      'f7cb0986c39bd3f7d51dd24f7854bdec'

        self.name = 'libXpm'
        self.version = '3.5.12'
        self.depends = ['libX11', 'xorgproto']
