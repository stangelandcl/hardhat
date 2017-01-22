from .base import X11BaseRecipe


class LibXtstRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXtstRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ef0a7ffd577e5f1a25b1663b37567952' \
                      '9663a1880151beaa73e9186c8309f6d9'
        self.name = 'libXtst'
        self.version = '1.2.2'
        self.depends = ['libX11', 'libXi', 'libXext']
