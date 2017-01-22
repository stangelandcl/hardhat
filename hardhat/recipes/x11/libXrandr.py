from .base import X11BaseRecipe


class LibXrandrRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXrandrRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1ff9e7fa0e4adea912b16a5f0cfa7c1d' \
                      '35b0dcda0e216831f7715c8a3abcf51a'

        self.name = 'libXrandr'
        self.version = '1.5.1'
        self.depends = ['libX11', 'libXext', 'libXrender', 'xorg-headers']
