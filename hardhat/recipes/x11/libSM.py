from .base import X11BaseRecipe


class LibSMRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibSMRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0baca8c9f5d934450a70896c4ad38d06' \
                      '475521255ca63b717a6510fdb6e287bd'

        self.name = 'libSM'
        self.version = '1.2.2'
        self.depends = ['libICE', 'xorg-headers', 'xtrans']
