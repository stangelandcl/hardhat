from .base import GnuRecipe
from ..urls import Urls


class GdbmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GdbmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7cd8cc2e35b1aaede6084ea57cc94477' \
                      '52f498daaea854100a4bad567614977d'

        self.name = 'gdbm'
        self.version = '1.17'
        self.url = Urls.gnu_template(self.name, self.version)
