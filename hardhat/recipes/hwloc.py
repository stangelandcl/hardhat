from .base import GnuRecipe


class HwLocRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(HwLocRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ab6910e248eed8c85d08b529917a6aae' \
                      '706b32b346e886ba830895e36a809729'

        self.name = 'hwloc'
        self.version = '1.11.7'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.url = 'https://www.open-mpi.org/software/hwloc/v1.11/' \
                   'downloads/hwloc-$version.tar.bz2'
