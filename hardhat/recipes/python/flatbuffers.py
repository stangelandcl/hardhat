from .base import SetupPyRecipe
from hardhat.recipes.flatbuffers import FlatbuffersRecipe
import os


class PyFlatbuffersRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(PyFlatbuffersRecipe, self).__init__(*args, **kwargs)

        f = FlatbuffersRecipe(settings=self)
        self.sha256 = f.sha256
        self.name = f.name
        self.depends = f.depends + ['flatbuffers']
        self.url = f.url
        self.version = f.version
        self.environment['FEATHER_HOME'] = self.prefix_dir

    def patch(self):
        self.directory = os.path.join(self.directory, 'python')
