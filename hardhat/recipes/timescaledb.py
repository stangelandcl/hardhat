import os
from .base import GnuRecipe


class TimescaleDBRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TimescaleDBRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ef7b1273a7008b606e099eee23a5eb8d' \
                      '2246fb5bdb01a9bbadcaf1b70fa143ec'

        self.name = 'timescaledb'
        self.version = '0.7.1'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'cmake', 'postgres']
        self.url = 'https://github.com/timescale/timescaledb/releases/' \
                   'download/$version/timescaledb-$version.tar.gz'
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '..'
            ]

    def patch(self):
        super(TimescaleDBRecipe, self).patch()
        dir = os.path.join(self.directory, 'build')
        os.makedirs(dir)
        self.directory = dir
