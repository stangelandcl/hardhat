from .base import GnuRecipe
from hardhat.urls import Urls


class GuileRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GuileRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e6786c934346fa2e38e46d8d81a622bb' \
                      '1c16d130153523f6129fcd79ef1fb040'

        self.name = 'guile'
        self.version = '2.0.11'
        self.url = Urls.gnu_template(self.name, self.version)
        self.depends = ['bash', 'coreutils', 'gc', 'gmp', 'libffi',
                        'libtool', 'libunistring', 'ncurses', 'readline']
