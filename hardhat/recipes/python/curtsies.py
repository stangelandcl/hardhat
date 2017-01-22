from .base import PipBaseRecipe


class CurtsiesRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CurtsiesRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '431631b9c1417b2ae8156d0bb6d7c3ce' \
                      '0c97941413717ed6713a9a9c60e9576e'

        self.depends = ['ncurses']
        self.pydepends = ['blessings', 'wcwidth']
        self.name = 'curtsies'
        self.version = '0.2.6'
