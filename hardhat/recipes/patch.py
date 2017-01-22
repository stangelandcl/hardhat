from .base import GnuRecipe
from ..urls import Urls


class PatchRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PatchRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7436f5a19f93c3ca83153ce9c5cbe484' \
                      '7e97c5d956e57a220121e741f6e7968f'

        self.name = 'patch'
        self.version = '2.7.5'
        self.url = Urls.gnu_template(self.name, self.version)
