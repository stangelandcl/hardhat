from .base import X11BaseRecipe


class LibXextRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXextRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b518d4d332231f313371fdefac59e377' \
                      '6f4f0823bcb23cf7c7305bfb57b16e35'

        self.name = 'libXext'
        self.version = '1.3.3'
        self.depends = ['libxslt', 'xmlto']
