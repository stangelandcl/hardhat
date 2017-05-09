from .base import PipBaseRecipe


class ScipyRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ScipyRecipe, self).__init__(*args, **kwargs)
        self.name = 'scipy'
        self.version = '0.19.0'
        self.pydepends = ['numpy', 'sphinx']

        self.environment['LDFLAGS'] += ' -shared'
        # disable deprecation warning
        self.environment['CFLAGS'] += \
            ' -DNPY_NO_DEPRECATED_API=NPY_1_6_API_VERSION'
        self.environment['CXXFLAGS'] = self.environment['CFLAGS']
        self.environment['CPPFLAGS'] =  \
            ' -DNPY_NO_DEPRECATED_API=NPY_1_6_API_VERSION'
