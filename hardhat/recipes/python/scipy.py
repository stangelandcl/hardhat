from .base import PipBaseRecipe


class ScipyRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ScipyRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8ab6e9c808bf2fb3e8576cd8cf07226d' \
                      '9cdc18b012c06d9708429a821ac6634e'

        self.name = 'scipy'
        self.version = '0.18.1'
        self.pydepends = ['numpy', 'sphinx']

        self.environment['LDFLAGS'] += ' -shared'
        # disable deprecation warning
        self.environment['CFLAGS'] += \
            ' -DNPY_NO_DEPRECATED_API=NPY_1_6_API_VERSION'
        self.environment['CXXFLAGS'] = self.environment['CFLAGS']
        self.environment['CPPFLAGS'] =  \
            ' -DNPY_NO_DEPRECATED_API=NPY_1_6_API_VERSION'
