from .base import GnuRecipe
from ..urls import Urls


class LibTasn1Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibTasn1Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fa802fc94d79baa00e7397cedf29eb68' \
                      '27d4bd8b4dd77b577373577c93a8c513'

        self.name = 'libtasn1'
        self.version = '4.8'
        self.url = Urls.gnu_template(self.name, self.version)
