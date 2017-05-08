from .gcc_prereq import GccPrereqRecipe
from ..cross.base import gmp_sha256, gmp_version


class GccGmpRecipe(GccPrereqRecipe):
    def __init__(self, *args, **kwargs):
        super(GccGmpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = gmp_sha256
        self.gcc_directory = None
        self.name = 'gmp'
        self.version = gmp_version

    @property
    def url(self):
        return 'https://gmplib.org/download/gmp/gmp-%s.tar.bz2' % self.version
