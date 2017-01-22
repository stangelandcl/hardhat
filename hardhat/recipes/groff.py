from .base import GnuRecipe
from ..urls import Urls


class GroffRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GroffRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3a48a9d6c97750bfbd535feeb5be0111' \
                      'db6406ddb7bb79fc680809cda6d828a5'
        self.name = 'groff'
        self.version = '1.22.3'
        self.url = Urls.gnu_template(self.name, self.version)
        self.configure_args += ['PAGE=letter']
        self.compile_args = ['make']
