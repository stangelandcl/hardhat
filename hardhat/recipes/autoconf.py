from .base import GnuRecipe
from ..urls import Urls


class AutoConfRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AutoConfRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '954bd69b391edc12d6a4a51a2dd14765' \
                      '43da5c6bbf05a95b59dc0dd6fd4c2969'

        self.name = 'autoconf'
        self.version = '2.69'
        self.url = Urls.gnu_template(self.name, self.version)
