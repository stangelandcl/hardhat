from .base import GnuRecipe
from ..urls import Urls


class GdbmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GdbmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f9fde3207f67ed8a5a5ddd8ad5e7acf7' \
                      'b27c2cf0f20dfbdde876dcd6e3d2dc0e'
        self.name = 'gdbm'
        self.version = '1.15'
        self.url = Urls.gnu_template(self.name, self.version)
