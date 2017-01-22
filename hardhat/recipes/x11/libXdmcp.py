from .base import X11BaseRecipe


class LibXdmcpRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXdmcpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '81fe09867918fff258296e1e1e159f0d' \
                      'c639cb30d201c53519f25ab73af4e4e2'

        self.name = 'libXdmcp'
        self.version = '1.1.2'
        self.depends = ['xorg-headers']
