from .base import GnuRecipe
from ..urls import Urls


class BisonRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BisonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '075cef2e814642e30e10e8155e93022e' \
                      '4a91ca38a65aa1d5467d4e969f97f338'
        self.name = 'bison'
        self.version = '3.0.5'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')
        self.environment_strip_lto()
