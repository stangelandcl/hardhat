from string import Template
from .gcc_prereq import GccPrereqRecipe
from ..cross.base import mpc_sha256, mpc_version


class GccMpcRecipe(GccPrereqRecipe):
    def __init__(self, *args, **kwargs):
        super(GccMpcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = mpc_sha256
        self.gcc_directory = None
        self.name = 'mpc'
        self.version = mpc_version
        self.extension = 'tar.gz'

    @property
    def url(self):
        return Template('ftp://gcc.gnu.org/pub/gcc/infrastructure/'
                        '$name-$version.%s' % (self.extension)).substitute(
                            name='mpc', version=self.version)
