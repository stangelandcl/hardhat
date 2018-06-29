from .base import GnuRecipe
from ..urls import Urls


class SedRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SedRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7aad73c8839c2bdadca9476f884d2953' \
                      'cdace9567ecd0d90f9959f229d146b40'
        self.name = 'sed'
        self.version = '4.5'
        self.url = Urls.gnu_template(self.name,
                                     self.version,
                                     extension='tar.xz')
