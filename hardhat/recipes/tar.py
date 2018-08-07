import os
from .base import GnuRecipe
from ..urls import Urls


class TarRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TarRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f1bf92dbb1e1ab27911a861ea8dde820' \
                      '8ee774866c46c0bb6ead41f4d1f4d2d3'
        self.name = 'tar'
        self.version = '1.30'
        self.url = Urls.gnu_template(self.name, self.version,
                                     'tar.xz')

    def install(self):
        super(TarRecipe, self).install()

        src = os.path.join(self.prefix_dir, 'bin', 'tar')
        dst = os.path.join(self.prefix_dir, 'bin', 'gtar')
        if os.path.exists(dst):
            os.remove(dst)
        os.symlink(src, dst)
