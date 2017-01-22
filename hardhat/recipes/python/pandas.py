from .base import PipBaseRecipe


class PandasRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PandasRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6f0f4f598c2b16746803c8bafef7c721' \
                      'c57e4844da752d36240c0acf97658014'

        self.name = 'pandas'
        self.version = '0.19.2'
        self.pydepends = ['numpy', 'dateutil', 'scipy', 'xlwt']

        self.environment['CFLAGS'] += \
            ' -DNPY_NO_DEPRECATED_API=NPY_1_6_API_VERSION'
        self.environment['CXXFLAGS'] = self.environment['CFLAGS']
