import os
from ..base import GnuRecipe


class Mingw64BaseRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Mingw64BaseRecipe, self).__init__(*args, **kwargs)

        self.depends = []
        self.mingw64depends = []

    @property
    def depends(self):
        return self._depends + ['mingw64-' + x for x in self.mingw64depends]

    @depends.setter
    def depends(self, value):
        self._depends = value

    def init(self):
        super(Mingw64BaseRecipe, self).init()

        dir = os.path.dirname(self.prefix_dir)
        self.base_extract_dir = os.path.join(dir, 'build')
        self.directory = self.extract_dir
