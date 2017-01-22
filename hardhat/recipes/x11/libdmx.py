from .base import X11BaseRecipe


class LibDmxRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibDmxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c97da36d2e56a2d7b6e4f896241785ac' \
                      'c95e97eb9557465fd66ba2a155a7b201'

        self.name = 'libdmx'
        self.version = '1.1.3'
        self.depends = ['libX11', 'libXext']
