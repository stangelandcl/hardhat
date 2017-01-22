from .base import GnuRecipe
from ..urls import Urls


class NettleRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NettleRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '46942627d5d0ca11720fec18d81fc38f' \
                      '7ef837ea4197c1f630e71ce0d470b11e'

        self.name = 'nettle'
        self.version = '3.3'
        self.depends = ['gmp']
        self.url = Urls.gnu_template(self.name, self.version)
