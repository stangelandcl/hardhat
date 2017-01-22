import os
import shutil
from .base import GnuRecipe


class DarkHttpdRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DarkHttpdRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a50417b622b32b5f421b3132cb94ebef' \
                      'f04f02c5fb87fba2e31147d23de50505'

        self.name = 'darkhttpd'
        self.version = '1.12'
        self.url = 'https://unix4lyfe.org/darkhttpd/darkhttpd-$version.tar.bz2'

    def configure(self):
        pass

    def install(self):
        src = os.path.join(self.directory, 'darkhttpd')
        dst = os.path.join(self.prefix_dir, 'bin', 'darkhttpd')
        shutil.copy2(src, dst)
