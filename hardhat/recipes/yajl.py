from .base import GnuRecipe


class YajlRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(YajlRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3fb73364a5a30efe615046d07e6db9d0' \
                      '9fd2b41c763c5f7d3bfb121cd5c5ac5a'
        self.name = 'yajl'
        self.version = '2.1.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools']
        self.url = 'https://github.com/lloyd/yajl/archive/$version.tar.gz'
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]
        self.compile_args = ['make', '-j1']
