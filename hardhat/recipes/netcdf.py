from .base import GnuRecipe


class NetcdfRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NetcdfRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'cbe70049cf1643c4ad7453f865108114' \
                      '36c9580cb7a1684ada2f32b95b00ca79'

        self.name = 'netcdf'
        self.version = '4.5.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://www.unidata.ucar.edu/downloads/netcdf/' \
                           'index.jsp'
        self.depends = ['autotools', 'hdf5', 'zlib']
        self.url = 'ftp://ftp.unidata.ucar.edu/pub/netcdf/' \
                   'netcdf-$version.tar.gz'
        self.configure_args += ['--enable-mmap',
                                '--enable-static',
                                '--enable-shared',
                                '--enable-fsync']
