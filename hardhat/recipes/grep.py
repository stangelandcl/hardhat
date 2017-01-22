from .base import GnuRecipe
from ..urls import Urls


class GrepRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GrepRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ad4cc44d23074a1c3a8baae8fbafff2a' \
                      '8c60f38a9a6108f985eef6fbee6dcaeb'

        self.name = 'grep'
        self.version = '2.27'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')
