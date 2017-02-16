import os
import shutil
from .base import GnuRecipe


class KDiff3Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(KDiff3Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '802c1ababa02b403a5dca15955c01592' \
                      '997116a24909745016931537210fd668'

        self.description = 'File compare and merge tool'
        self.name = 'kdiff3'
        self.version = '0.9.98'
        self.depends = ['qt5']
        self.url = 'https://dronedata.dl.sourceforge.net/project/kdiff3/' \
                   'kdiff3/$version/kdiff3-$version.tar.gz'
        self.compile_args = self.shell_args + ['./configure', 'qt4']

    def configure(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'installing kdiff3')
        src = os.path.join(self.directory, 'releaseQt', 'kdiff3')
        dst = os.path.join(self.prefix_dir, 'bin', 'kdiff3')

        shutil.copy2(src, dst)
