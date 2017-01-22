from .base import SetupPyRecipe
from hardhat.recipes.feather import FeatherRecipe as F1
from hardhat.util import patch
import os


class PyFeatherRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(PyFeatherRecipe, self).__init__(*args, **kwargs)

        f = F1(settings=self)
        self.sha256 = f.sha256
        self.name = f.name
        self.depends = f.depends + ['feather']
        self.pydepends = ['numpy']
        self.url = f.url
        self.version = f.version
        self.environment['FEATHER_HOME'] = self.prefix_dir

    def patch(self):
        self.directory = os.path.join(self.directory, 'python')
        self.log_dir('patch', self.directory, 'use shared libfeather.so')
        filename = os.path.join(self.directory, 'setup.py')

        src = "FEATHER_STATIC_BUILD = True"
        dst = "FEATHER_STATIC_BUILD = False"
        patch(filename, src, dst)

    def configure(self):
        super(PyFeatherRecipe, self).configure()
