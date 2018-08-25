import os
from hardhat.util import patch
import shutil
from hardhat.environment import toolchain_lib_path
from hardhat.urls import Urls
from .base import CrossGnuRecipe
from ..make import MakeRecipe


class CrossMakeRecipe(CrossGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossMakeRecipe, self).__init__(*args, **kwargs)
        make = MakeRecipe(settings=self)
        self.sha256 = make.sha256
        self.version = make.version
        self.url = make.url

        self.name = 'cross-make'
        self.configure_args = self.shell_args + [
            './configure', '--without-guile',
            '--prefix=%s' % self.cross_prefix_dir]
        self.configure_strip_cross_compile()

    def patch(self):
        src = '#if !defined __alloca && !defined __GNU_LIBRARY__'
        dst = '#if 1'
        filename = os.path.join(self.directory, 'glob', 'glob.c')
        patch(filename, src, dst)

    def install(self):
        super(CrossMakeRecipe, self).install()

        src = os.path.join(self.cross_prefix_dir, 'bin', 'make')
        dst = os.path.join(self.cross_prefix_dir, 'bin', 'gmake')
        if os.path.exists(dst):
            os.remove(dst)
        os.symlink(src, dst)

    def post_install(self):
        pass
        # disable ldconfig
