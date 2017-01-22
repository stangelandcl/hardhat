from .base import GnuRecipe


class MvaPich2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MvaPich2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '791a6fc2b23de63b430b3e598bf05b1b' \
                      '25b82ba8bf7e0622fc81ba593b3bb131'

        self.name = 'mvapich2'
        self.version = '2.2'
        self.depends = ['libibverbs']
        self.url = 'http://mvapich.cse.ohio-state.edu/download/mvapich/mv2/' \
                   'mvapich2-$version.tar.gz'
        del self.environment['F90']
        self.configure_strip_cross_compile()
