import os
import shutil
from .base import SetupPyRecipe


class HardhatRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(HardhatRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8c7e40921866f042293b8f4669873031' \
                      'b1cfa87f1f13303df536a560f43fce26'

        self.description = 'Install hardhat (ourself) the current version'
        self.name = 'hardhat'
        self.version = '747d6caf98516ffce4347c3a8688f1356fed90bb'
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
