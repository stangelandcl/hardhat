from .base import GnuRecipe


class NetcdfCpp4Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NetcdfCpp4Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '25da1c97d7a01bc4cee34121c3290987' \
                      '2edd38404589c0427fefa1301743f18f'

        self.name = 'netcdf-c++4'
        self.version = '4.3.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['netcdf']
        self.url = 'https://github.com/Unidata/netcdf-cxx4/archive/' \
                   'v$version.tar.gz'
        self.configure_args += ['--enable-static',
                                '--enable-shared']
