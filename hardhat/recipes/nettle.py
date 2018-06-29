from .base import GnuRecipe
from ..urls import Urls


class NettleRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NettleRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ae7a42df026550b85daca8389b6a60ba' \
                      '6313b0567f374392e54918588a411e94'

        self.name = 'nettle'
        self.version = '3.4'
        self.depends = ['gmp']
        self.url = Urls.gnu_template(self.name, self.version)
