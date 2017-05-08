from .gcc_prereq import GccPrereqRecipe
from ..cross.base import isl_sha256, isl_version


class GccIslRecipe(GccPrereqRecipe):
    def __init__(self, *args, **kwargs):
        super(GccIslRecipe, self).__init__(*args, **kwargs)
        self.sha256 = isl_sha256
        self.gcc_directory = None
        self.name = 'isl'
        self.version = isl_version
