from .base import GnuRecipe
from ..urls import Urls


class LibUnistringRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibUnistringRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0b3f4dbea5124f56639a701376ed78e5' \
                      'f595e7b720cfbb0cf1f81f375894c77b'

        self.name = 'libunistring'
        self.version = '0.9.5'
        self.url = Urls.gnu_template(self.name, self.version,
                                     'tar.xz')
