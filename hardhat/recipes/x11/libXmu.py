from .base import X11BaseRecipe


class LibXmuRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXmuRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '756edc7c383254eef8b4e1b733c3bf1d' \
                      'c061b523c9f9833ac7058378b8349d0b'

        self.name = 'libXmu'
        self.version = '1.1.2'
        self.depends = ['libXext', 'libXt']
