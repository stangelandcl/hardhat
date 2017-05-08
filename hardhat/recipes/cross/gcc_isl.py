from .gcc_prereq import GccPrereqRecipe
from .base import isl_sha256, isl_version


class CrossGccIslRecipe(GccPrereqRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossGccIslRecipe, self).__init__(*args, **kwargs)
        self.sha256 = isl_sha256
        self.gcc_directory = None
        self.name = 'cross-isl'
        self.version = isl_version
