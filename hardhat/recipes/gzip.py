from .base import GnuRecipe
from ..urls import Urls


class GzipRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GzipRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ff1767ec444f71e5daf8972f6f8bf68c' \
                      'fcca1d2f76c248eb18e8741fc91dbbd3'

        self.name = 'gzip'
        self.version = '1.8'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')
