from .base import GnuRecipe
from ..urls import Urls


class GlobalRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GlobalRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'af16e0a686a46f759156cb685e25f345' \
                      '680703f43f93af1ce8d834caaf541da6'

        self.name = 'global'
        self.version = '6.5.4'
        self.url = Urls.gnu_template(self.name, self.version)
        self.environment['LIBS'] += ' -ltinfow -lncursesw'
