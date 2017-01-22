from .base import X11BaseRecipe


class LibXshmFenceRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXshmFenceRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd21b2d1fd78c1efbe1f2c16dae1cb23f' \
                      '8fd231dcf891465b8debe636a9054b0c'

        self.name = 'libxshmfence'
        self.version = '1.2'
        self.depends = ['xorg-headers']
