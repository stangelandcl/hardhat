from .base import X11BaseRecipe


class LibXresRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXresRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '26899054aa87f81b17becc68e8645b24' \
                      '0f140464cf90c42616ebb263ec5fa0e5'
        self.name = 'libXres'
        self.version = '1.0.7'
        self.depends = ['libXext', 'libX11', 'xorgproto']
