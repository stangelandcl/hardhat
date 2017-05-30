import os
import shutil
from .base import SetupPyRecipe


class HardhatRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(HardhatRecipe, self).__init__(*args, **kwargs)
        self.sha256 = None

        self.description = 'Install hardhat (ourself) the current version'
        self.name = 'hardhat'
        self.version = 'a4db53c6e07cca27dbd9c2f282f9db2353cd12f1'
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
