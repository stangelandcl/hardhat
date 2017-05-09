import os
from .base import SetupPyRecipe
from hardhat.util import patch


class PillowRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(PillowRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '00b6a5f28d00f720235a937ebc2f50f4' \
                      '292a5c7e2d6ab9a8b26153b625c4f431'
        self.name = 'pillow'
        self.version = '4.1.1'
        self.depends = ['libjpeg-turbo', 'libpng']
        self.pydepends = ['olefile']
#        self.extra_install_args = ['--disable-platform-guessing']

    def patch(self):
        self.log_dir('patch', self.directory, 'disable use of /usr folders')
        src = 'self.disable_platform_guessing = None'
        dst = 'self.disable_platform_guessing = True'
        filename = os.path.join(self.directory, 'setup.py')
        patch(filename, src, dst)
