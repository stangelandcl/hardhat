from .base import X11BaseRecipe


class LibXScrnSaverRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXScrnSaverRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8ff1efa7341c7f34bcf9b17c89648d63' \
                      '25ddaae22e3904e091794e0b4426ce1d'

        self.name = 'libXScrnSaver'
        self.version = '1.2.2'
        self.depends = ['libX11', 'libXext', 'xorgproto']
