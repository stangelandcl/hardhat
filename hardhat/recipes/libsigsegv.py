from .base import GnuRecipe
from ..urls import Urls


class LibSigSegvRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibSigSegvRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8460a4a3dd4954c3d96d7a4f5dd5bc4d' \
                      '9b76f5754196aa245287553b26d2199a'

        self.name = 'libsigsegv'
        self.version = '2.10'
        self.url = Urls.gnu_template(self.name, self.version)
        self.configure_strip_cross_compile()
