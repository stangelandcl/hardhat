from .gcc_prereq import GccPrereqRecipe
from ..cross.base import gmp_sha256, gmp_version


class CrossGccGmpRecipe(GccPrereqRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossGccGmpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = gmp_sha256
        self.gcc_directory = None
        self.name = 'cross-gmp'
        self.version = gmp_version

    @property
    def url(self):
        return 'https://gmplib.org/download/gmp/gmp-%s.tar.bz2' % self.version
