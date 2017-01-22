from .base import GnuRecipe
from ..urls import Urls


class WhichRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(WhichRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f4a245b94124b377d8b49646bf421f91' \
                      '55d36aa7614b6ebf83705d3ffc76eaad'

        self.name = 'which'
        self.version = '2.21'
        self.url = Urls.gnu_template(self.name, self.version)
