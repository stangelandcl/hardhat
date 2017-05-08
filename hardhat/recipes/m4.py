from .base import GnuRecipe
from hardhat.urls import Urls


class M4Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(M4Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ab2633921a5cd38e48797bf5521ad259' \
                      'bdc4b979078034a3b790d7fec5493fab'

        self.name = 'm4'
        self.version = '1.4.18'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.gz')
        self.environment_strip_lto()
