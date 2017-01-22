from .base import X11BaseRecipe


class LibXkbFileRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXkbFileRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '51817e0530961975d9513b773960b4ed' \
                      'd275f7d5c72293d5a151ed4f42aeb16a'

        self.name = 'libxkbfile'
        self.version = '1.0.9'
        self.depends = ['libX11']
