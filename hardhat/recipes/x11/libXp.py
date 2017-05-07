from .base import X11BaseRecipe


class LibXpRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7f360c9905849c3587d48efc0f0ecbc8' \
                      '52c19f61a52b18530d6b005cb9148c57'
        self.name = 'libXp'
        self.version = '1.0.3'
        self.depends = ['libXext', 'libX11', 'xorg-headers']
