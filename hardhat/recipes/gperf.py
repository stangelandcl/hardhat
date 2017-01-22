from .base import GnuRecipe
from ..urls import Urls


class GperfRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GperfRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '588546b945bba4b70b6a3a616e80b4ab' \
                      '466e3f33024a352fc2198112cdbb3ae2'

        self.name = 'gperf'
        self.version = '3.1'
        self.url = Urls.gnu_template(self.name, self.version)
