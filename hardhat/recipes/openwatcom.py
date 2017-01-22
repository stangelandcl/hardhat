import os
import shutil
from .base import GnuRecipe


class OpenWatcomRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpenWatcomRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '10751815179199436e8b186974c20e8e' \
                      'd93925c3e94f55f2e1a4c70e3ab737d8'

        self.name = 'openwatcom'
        self.version = '2cf5825f00e10df70406a3411f22dfc2e3893690'
        self.url = 'https://github.com/open-watcom/open-watcom-v2/archive/' \
                   '$version.tar.gz'

        self.configure_args = self.shell_args + [
            './build.sh'
            ]

        self.environment['OWROOT'] = self.directory

    def patch(self):
        src = os.path.join(self.directory, 'setvars.sh')
        dst = os.path.join(self.directory, 'setvars')
        if os.path.exists(dst):
            os.remove(dst)
        shutil.copy2(src, dst)
