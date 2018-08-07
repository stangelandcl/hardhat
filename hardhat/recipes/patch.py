from .base import GnuRecipe
from ..urls import Urls


class PatchRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PatchRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8cf86e00ad3aaa6d26aca30640e86b0e' \
                      '3e1f395ed99f189b06d4c9f74bc58a4e'
        self.name = 'patch'
        self.version = '2.7.6'
        self.url = Urls.gnu_template(self.name, self.version)
