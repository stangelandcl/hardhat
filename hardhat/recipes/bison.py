from .base import GnuRecipe
from ..urls import Urls


class BisonRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BisonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'deec377b95aa72ec4e1a33fe2c938d24' \
                      '80749d740b5291a7cc1d77808d3710bf'

        self.name = 'bison'
        self.version = '3.2'
        self.version_url = 'http://ftp.gnu.org/gnu/bison/'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')
        self.environment_strip_lto()
