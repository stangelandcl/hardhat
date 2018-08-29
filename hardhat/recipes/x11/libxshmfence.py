from .base import X11BaseRecipe


class LibXshmFenceRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXshmFenceRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b884300d26a14961a076fbebc762a398' \
                      '31cb75f92bed5ccf9836345b459220c7'
        self.name = 'libxshmfence'
        self.version = '1.3'
        self.depends = ['xorgproto']
