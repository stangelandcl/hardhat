from .gcc_prereq import GccPrereqRecipe
from ..cross.base import mpfr_sha256, mpfr_version


class CrossGccMpfrRecipe(GccPrereqRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossGccMpfrRecipe, self).__init__(*args, **kwargs)
        self.sha256 = mpfr_sha256
        self.gcc_directory = None
        self.name = 'cross-mpfr'
        self.version = mpfr_version

    @property
    def url(self):
        return 'http://www.mpfr.org/mpfr-%s/mpfr-%s.tar.bz2' \
            % (self.version, self.version)
