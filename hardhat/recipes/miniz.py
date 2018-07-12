from .base import GnuRecipe


class MinizRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MinizRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '91f2bc145ae7a35114f8edf761611184' \
                      '11d141394f2464fcef2355acdd037051'

        self.name = 'miniz'
        self.version = '2.0.7'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = []
        self.url = 'https://github.com/richgel999/miniz/archive/$version.tar.gz'
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]
