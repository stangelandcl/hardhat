from .base import GnuRecipe


class NetcdfCppRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NetcdfCppRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '95ed6ab49a0ee001255eac4e44aacb5c' \
                      'a4ea96ba850c08337a3e4c9a0872ccd1'

        self.name = 'netcdf-c++'
        self.version = '4.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['netcdf']
        self.url = 'ftp://ftp.unidata.ucar.edu/pub/netcdf/' \
                   'netcdf-cxx-$version.tar.gz'
        self.configure_args += ['--enable-static',
                                '--enable-shared']
