from .base import GnuRecipe
from ..urls import Urls


class LibPipelineRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibPipelineRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'da46d7b20163aadb9db2faae483f734e' \
                      '9096a7550c84b94029abeab62dd1b9ee'

        self.name = 'libpipeline'
        self.version = '1.4.1'
        self.url = Urls.savannah(self.name, self.version)
