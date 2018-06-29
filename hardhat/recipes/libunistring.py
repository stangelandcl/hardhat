from .base import GnuRecipe
from ..urls import Urls


class LibUnistringRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibUnistringRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'eb8fb2c3e4b6e2d336608377050892b5' \
                      '4c3c983b646c561836550863003c05d7'
        self.name = 'libunistring'
        self.version = '0.9.10'
        self.url = Urls.gnu_template(self.name, self.version,
                                     'tar.xz')
