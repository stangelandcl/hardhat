import os
import platform
from ..base import Make, Downloader, Extractor, Recipe
from hardhat.recipes.cross.cross_linux_headers import LinuxHeadersBase
from hardhat.recipes.cross.base import CrossGnuRecipe
from hardhat.environment import toolchain_env


class LinuxHeadersRecipe(LinuxHeadersBase, CrossGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LinuxHeadersRecipe, self).__init__(*args, **kwargs)
        self.name = 'linux-headers'
        prefix_dir = os.path.join(self.prefix_dir,
                                  self.target_triplet)

        self.environment['CFLAGS'] = '-O2'
        self.include_dir = '%s/include' % prefix_dir
