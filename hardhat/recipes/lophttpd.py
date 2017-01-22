import os
import shutil
from .base import GnuRecipe


class LophttpdRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LophttpdRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a18a83cff8aaebf640d7970bc29a07d5' \
                      'c955ee68ac157ab10bb44b30f3def502'

        self.name = 'lophttpd'
        self.version = '1.03s'
        self.url = 'https://github.com/stealth/lophttpd/archive/' \
                   'lophttpd-$version.tar.gz'

    def install(self):
        self.log_dir('install', self.directory)
        files = ['frontend',
                 'lhttpd',
                 'newdh']
        for file in files:
            src = os.path.join(self.directory, file)
            dst = os.path.join(self.prefix_dir, 'bin', file)
            shutil.copy2(src, dst)
