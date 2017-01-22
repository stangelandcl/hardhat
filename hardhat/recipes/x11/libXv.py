from .base import X11BaseRecipe


class LibXvRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXvRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd26c13eac99ac4504c532e8e76a1c8e4' \
                      'bd526471eb8a0a4ff2a88db60cb0b088'

        self.name = 'libXv'
        self.version = '1.0.11'
        self.depends = ['libX11', 'libXext']
