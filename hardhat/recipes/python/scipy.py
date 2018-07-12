from .base import PipBaseRecipe


class ScipyRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ScipyRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '878352408424dffaa695ffedf2f9f928' \
                      '44e116686923ed9aa8626fc30d32cfd1'

        self.name = 'scipy'
        self.version = '1.1.0'
        self.pydepends = ['numpy', 'sphinx']

        self.environment['LDFLAGS'] += ' -shared'
        # disable deprecation warning
        self.environment['CFLAGS'] += \
            ' -DNPY_NO_DEPRECATED_API=NPY_1_6_API_VERSION'
        self.environment['CXXFLAGS'] = self.environment['CFLAGS']
        self.environment['CPPFLAGS'] =  \
            ' -DNPY_NO_DEPRECATED_API=NPY_1_6_API_VERSION'
        self.environment_strip_lto()
        self.environment['CFLAGS'] += ' -fPIC'
        self.environment['CXXFLAGS'] += ' -fPIC'
        self.environment['FFLAGS'] += ' -fPIC'
