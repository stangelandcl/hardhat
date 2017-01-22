import datetime
import os
from hardhat.recipes.base import GnuRecipe
from hardhat.environment import toolchain_env


def make_cross_prefix_dir(prefix_dir):
    return os.path.join(prefix_dir, 'cross')


class CrossGnuRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossGnuRecipe, self).__init__(*args, **kwargs)
        self.cross_prefix_dir = make_cross_prefix_dir(self.prefix_dir)
        self.environment = toolchain_env(self.cross_prefix_dir)
