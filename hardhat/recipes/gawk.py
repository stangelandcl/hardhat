from .base import GnuRecipe
from ..urls import Urls


class GawkRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GawkRecipe, self).__init__(*args, **kwargs)
        self.name = 'gawk'
        self.version = '4.2.1'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')
