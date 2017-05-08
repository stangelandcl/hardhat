from .gcc_prereq import GccPrereqRecipe
from ..cross.base import mpc_sha256, mpc_version


class CrossGccMpcRecipe(GccPrereqRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossGccMpcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = mpc_sha256
        self.gcc_directory = None
        self.name = 'cross-mpc'
        self.version = mpc_version
        self.extension = 'tar.gz'
