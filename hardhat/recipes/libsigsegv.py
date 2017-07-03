from .base import GnuRecipe
from ..urls import Urls


class LibSigSegvRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibSigSegvRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'dd7c2eb2ef6c47189406d562c1dc0f96' \
                      'f2fc808036834d596075d58377e37a18'

        self.name = 'libsigsegv'
        self.version = '2.11'
        self.url = Urls.gnu_template(self.name, self.version)
        self.configure_strip_cross_compile()
