from .base import X11BaseRecipe


class LibPciAccessRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibPciAccessRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '07f864654561e4ac8629a0ef9c8f07fb' \
                      'c1f8592d1b6c418431593e9ba2cf2fcf'

        self.name = 'libpciaccess'
        self.version = '0.13.4'
