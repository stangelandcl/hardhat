from .base import PipBaseRecipe


class PandasRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PandasRecipe, self).__init__(*args, **kwargs)
        self.name = 'pandas'
        self.version = '0.20.1'
        self.pydepends = ['numpy', 'dateutil', 'scipy', 'xlwt']

        self.environment['CFLAGS'] += \
            ' -DNPY_NO_DEPRECATED_API=NPY_1_6_API_VERSION'
        self.environment['CXXFLAGS'] = self.environment['CFLAGS']
