import os
from .base import GnuRecipe


class AlsoftConfRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AlsoftConfRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1eb759d067251ed13af43d6a08f70f8d' \
                      '77d315742597f979444b1ac51ece4136'

        self.name = 'alsoft-conf'
        self.version = '1.4.3'
        self.url = 'http://www.anduin.net/~angasule/fp-content/attachs/' \
                   'alsoft-conf_$version.tar.gz'

        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '..'
            ]

        self.environment['CXXFLAGS'] += ' -fPIC'

    def patch(self):
        self.directory = os.path.join(self.directory, 'build')
        self.log_dir('patch', self.directory, 'creating build dir')
        os.makedirs(self.directory)
