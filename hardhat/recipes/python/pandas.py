from .base import PipBaseRecipe


class PandasRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PandasRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9cd3614b4e31a0889388ff1bd19ae857' \
                      'ad52658b33f776065793c293a29cf612'

        self.name = 'pandas'
        self.version = '0.23.3'
        self.pydepends = ['numpy', 'dateutil', 'scipy', 'xlwt']

        self.environment['CFLAGS'] += \
            ' -DNPY_NO_DEPRECATED_API=NPY_1_6_API_VERSION'
        self.environment['CXXFLAGS'] = self.environment['CFLAGS']
