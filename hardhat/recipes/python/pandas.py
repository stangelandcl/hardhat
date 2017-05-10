from .base import PipBaseRecipe


class PandasRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PandasRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '42707365577ef69f7c9c168ddcf045df' \
                      '2957595a9ee71bc13c7997eecb96b190'

        self.name = 'pandas'
        self.version = '0.20.1'
        self.pydepends = ['numpy', 'dateutil', 'scipy', 'xlwt']

        self.environment['CFLAGS'] += \
            ' -DNPY_NO_DEPRECATED_API=NPY_1_6_API_VERSION'
        self.environment['CXXFLAGS'] = self.environment['CFLAGS']
