from .base import PipBaseRecipe


class WcWidthRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(WcWidthRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3df37372226d6e63e1b1e1eda15c594b' \
                      'ca98a22d33a23832a90998faa96bc65e'

        self.depends = ['ncurses']
        self.name = 'wcwidth'
        self.version = '0.1.7'
