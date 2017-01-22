from .base import GnuRecipe
from ..urls import Urls


class GawkRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GawkRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '53e184e2d0f90def9207860531802456' \
                      '322be091c7b48f23fdc79cda65adc266'

        self.name = 'gawk'
        self.version = '4.1.4'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')
