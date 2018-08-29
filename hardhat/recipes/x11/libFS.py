from .base import X11BaseRecipe


class LibFSRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibFSRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2e9d4c07026a7401d4fa4ffae86e6ac7' \
                      'fec83f50f3268fa85f52718e479dc4f3'

        self.name = 'libFS'
        self.version = '1.0.7'
        self.depends = ['pkgconfig', 'xorgproto', 'xtrans']
