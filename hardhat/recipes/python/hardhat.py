import os
import shutil
from .base import SetupPyRecipe


class HardhatRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(HardhatRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '97c1f18496814c495f77c379e5d3a30c' \
                      'fd3b6fcb316232de150e7a6e17cbcb9d'

        self.description = 'Install hardhat (ourself) the current version'
        self.name = 'hardhat'
        self.version = 'afe6fb7c76c2ce812b2029858a89741524d2ddec'
        self.url = 'https://github.com/stangelandcl/hardhat/archive/' \
                   '$version.tar.gz'
        self.dest_dir = os.path.join(self.prefix_dir, 'hardhat')

    def configure(self):
        self.log_dir('configure', self.directory, 'copy to %s' % self.dest_dir)
        if os.path.exists(self.dest_dir):
            shutil.rmtree(self.dest_dir)
        shutil.copytree(self.directory, self.dest_dir)

    def compile(self):
        # develop so users can modify without requiring the source to modify
        # and reinstall
        self.compile_args = [self.python,
                             'setup.py',
                             'develop']
        self.log_dir('compile', self.dest_dir, 'compiling')
        self.run_exe(self.compile_args, self.dest_dir, self.environment)

    def install(self):
        pass
