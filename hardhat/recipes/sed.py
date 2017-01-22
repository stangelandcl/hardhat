from .base import GnuRecipe
from ..urls import Urls


class SedRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SedRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '47c20d8841ce9e7b6ef8037768aac44b' \
                      'c2937fff1c265b291c824004d56bd0aa'

        self.name = 'sed'
        self.version = '4.3'
        self.url = Urls.gnu_template(self.name,
                                     self.version,
                                     extension='tar.xz')
