from .base import X11BaseRecipe


class LibXdamageRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXdamageRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7c3fe7c657e83547f4822bfde30a90d8' \
                      '4524efb56365448768409b77f05355ad'

        self.name = 'libXdamage'
        self.version = '1.1.4'
        self.depends = ['libX11', 'libXfixes', 'xorgproto']
