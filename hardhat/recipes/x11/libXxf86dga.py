from .base import X11BaseRecipe


class LibXxf86dgaRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXxf86dgaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8eecd4b6c1df9a3704c04733c2f4fa93' \
                      'ef469b55028af5510b25818e2456c77e'

        self.name = 'libXxf86dga'
        self.version = '1.1.4'
        self.depends = ['libX11', 'libXext']
