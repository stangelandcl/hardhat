from .base import GnuRecipe
from ..urls import Urls


class GawkRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GawkRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd1119785e746d46a8209d28b2de404a5' \
                      '7f983aa48670f4e225531d3bdc175551'
        self.name = 'gawk'
        self.version = '4.2.1'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')
