from .base import GnuRecipe
from ..urls import Urls


class BisonRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BisonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a72428c7917bdf9fa93cb8181c971b6e' \
                      '22834125848cf1d03ce10b1bb0716fe1'

        self.name = 'bison'
        self.version = '3.0.4'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')
        self.environment_strip_lto()
