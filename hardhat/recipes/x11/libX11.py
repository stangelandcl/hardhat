from .base import X11BaseRecipe


class LibX11Recipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibX11Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b7c748be3aa16ec2cbd81edc847e9b6e' \
                      'e03f88143ab270fb59f58a044d34e441'

        self.name = 'libX11'
        self.version = '1.6.4'
        self.depends = ['libxcb', 'xorg-headers', 'xtrans']

        self.configure_args += [
            '--enable-ipv6',
            ]
