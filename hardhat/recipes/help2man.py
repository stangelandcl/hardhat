from .base import GnuRecipe
from ..urls import Urls


class Help2ManRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        self.sha256 = 'd4ecf697d13f14dd1a78c5995f06459b' \
                      'ff706fd1ce593d1c02d81667c0207753'
               
        super(Help2ManRecipe, self).__init__(*args, **kwargs)
        self.name = 'help2man'
        self.version = '1.47.4'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')
