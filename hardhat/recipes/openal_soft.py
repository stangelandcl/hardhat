from .base import GnuRecipe


class OpenALSoftRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpenALSoftRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a598241d1af2e90c25a1b91da4c9ddc0' \
                      'e7cb6a4b5f1477fc680d139c57cd38cc'

        self.name = 'openal-soft'
        self.version = '1.18.2'
        self.url = 'https://github.com/kcat/openal-soft/archive/' \
                   'openal-soft-$version.tar.gz'
        self.depends = ['alsa-lib', 'qt5']

        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '..'
            ]

        self.environment['CXXFLAGS'] += ' -fPIC'
