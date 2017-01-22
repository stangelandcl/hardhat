from .base import GnuRecipe
import os


class OpenALRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpenALRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '11ea176f6cbf9763dbce0953dd77ab72' \
                      'd032b4ad95f07afffb91844abb174033'

        self.name = 'openal'
        self.version = '1.17.2'
        v = self.version.replace('.', '')
        self.url = 'https://github.com/kcat/$name-soft/archive/' \
                   '$name-soft-$version.tar.gz'
        self.depends = ['alsa-lib',
                        'alsoft-conf',
                        #                        'pulseaudio',
                        'qt5'
                        ]
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '..'
            ]

    def patch(self):
        self.directory = os.path.join(self.directory, 'build')
