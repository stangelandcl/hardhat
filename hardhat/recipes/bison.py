from .base import GnuRecipe
from ..urls import Urls


class BisonRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BisonRecipe, self).__init__(*args, **kwargs)
        self.name = 'bison'
        self.version = '3.0.5'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')
        self.environment_strip_lto()
