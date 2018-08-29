from .base import X11BaseRecipe


class LibX11Recipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibX11Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '4d3890db2ba225ba8c55ca63c6409c1e' \
                      'bb078a2806de59fb16342768ae63435d'

        self.name = 'libX11'
        self.version = '1.6.5'
        self.depends = ['libxcb', 'xorgproto', 'xtrans']

        self.configure_args += [
            '--enable-ipv6',
            ]
