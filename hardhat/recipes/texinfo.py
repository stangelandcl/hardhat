from .base import GnuRecipe
from ..urls import Urls


class TexInfoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TexInfoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '77774b3f4a06c20705cc2ef1c8048644' \
                      '22e3cf95235e965b1f00a46df7da5f62'

        self.name = 'texinfo'
        self.version = '6.5'
        self.depends = ['perl5']
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')
