from .base import GnuRecipe
from ..urls import Urls


class GzipRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GzipRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ae506144fc198bd8f81f1f4ad19ce63d' \
                      '5a2d65e42333255977cf1dcf1479089a'

        self.name = 'gzip'
        self.version = '1.9'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')
