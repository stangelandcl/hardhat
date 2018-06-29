import os
import shutil
from .base import GnuRecipe


class CC65Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CC65Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '73b89634655bfc6cef9aa0b8950f1965' \
                      '7a902ee5ef0c045886e418bb116d2eac'
        self.description = 'Atari VCS/2600 C compiler'
        self.name = 'cc65'
        self.version = '2.17'
        self.version_regex = 'V(?P<version>\d+\.\d+(\.\d+)?)\.tar\.gz'
        self.version_url = 'https://github.com/cc65/cc65/releases'
        self.url = 'https://github.com/cc65/cc65/archive/V$version.tar.gz'
        src = os.path.join(self.directory, 'bin')
        dst = os.path.join(self.prefix_dir, 'bin')
        self.install_args = ['cp', src + '/*', dst + '/']

    def configure(self):
        pass
