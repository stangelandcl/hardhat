from .base import GnuRecipe


class Hdf5Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Hdf5Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a4335849f19fae88c264fd0df046bc32' \
                      '1a78c536b2548fc508627a790564dc38'
        self.name = 'hdf5'
        self.version = '1.8.20'
        version = '.'.join(self.version.split('.')[:2])
        self.url = 'https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-%s/' \
                   'hdf5-$version/src/hdf5-$version.tar.bz2' % version
        self.depends += ['zlib']
        self.configure_strip_cross_compile()
        self.configure_args += ['--enable-cxx',
                                '--enable-fortran',
                                '--enable-fortran2003',
                                '--enable-production',
                                '--enable-static',
                                '--enable-shared']

    def need_configure(self):
        return True
