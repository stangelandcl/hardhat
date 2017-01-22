from .base import GnuRecipe
from ..urls import Urls


class LibIDNRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibIDNRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '44a7aab635bb721ceef6beecc4d49dfd' \
                      '19478325e1b47f3196f7d2acc4930e19'

        self.name = 'libidn'
        self.version = '1.33'
        self.url = Urls.gnu_template(self.name, self.version)
