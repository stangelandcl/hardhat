import os
import shutil
from .base import GnuRecipe


class DasmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DasmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd6c99e7feb3469848a4fc762c204b8a0' \
                      'b914cc2f90ab0edbd0faa6fc8524a106'

        self.description = 'Atari VCS/2600 assembler'
        self.name = 'dasm'
        self.version = '45fa6482594af347152a97d684fd01bc0060bf1a'
        self.url = self.github_commit('munsie')

    def configure(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'installing dasm and ftohex')
        src = os.path.join(self.directory, 'bin', 'dasm')
        dst = os.path.join(self.prefix_dir, 'bin', 'dasm')
        shutil.copy2(src, dst)
        src = os.path.join(self.directory, 'bin', 'ftohex')
        dst = os.path.join(self.prefix_dir, 'bin', 'ftohex')
        shutil.copy2(src, dst)
