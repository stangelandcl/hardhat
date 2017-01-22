import os
from .base import GnuRecipe
from ..urls import Urls


class TarRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TarRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '402dcfd0022fd7a1f2c5611f5c61af1c' \
                      'd84910a760a44a688e18ddbff4e9f024'

        self.name = 'tar'
        self.version = '1.29'
        self.url = Urls.gnu_template(self.name, self.version,
                                     'tar.xz')

    def install(self):
        super(TarRecipe, self).install()

        src = os.path.join(self.prefix_dir, 'bin', 'tar')
        dst = os.path.join(self.prefix_dir, 'bin', 'gtar')
        if os.path.exists(dst):
            os.remove(dst)
        os.symlink(src, dst)
