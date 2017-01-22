from .base import GnuRecipe


class Hdf5Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Hdf5Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd9cda297ee76ade9881c420898793925' \
                      '0d397bae6252d0ccb66fa7d24d67e263'

        self.name = 'hdf5'
        self.version = '1.8.17'
        self.url = 'http://www.hdfgroup.org/ftp/HDF5/current/src/' \
                   'hdf5-$version.tar.gz'
        self.configure_strip_cross_compile()

    def need_configure(self):
        return True
