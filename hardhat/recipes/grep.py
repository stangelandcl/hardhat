from .base import GnuRecipe
from ..urls import Urls


class GrepRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GrepRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'db625c7ab3bb3ee757b3926a5cfa8d9e' \
                      '1c3991ad24707a83dde8a5ef2bf7a07e'

        self.name = 'grep'
        self.version = '3.1'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')
