from .base import PipBaseRecipe


class BlessingsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(BlessingsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'edc5713061f10966048bf6b40d9a514b' \
                      '381e0ba849c64e034c4ef6c1847d3007'

        self.depends = ['ncurses']
        self.name = 'blessings'
        self.version = '1.6'
