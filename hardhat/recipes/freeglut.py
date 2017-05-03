from .base import GnuRecipe


class FreeGlutRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FreeGlutRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2a43be8515b01ea82bcfa17d29ae0d40' \
                      'bd128342f0930cd1f375f1ff999f76a2'
        self.name = 'freeglut'
        self.version = '3.0.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.url = 'http://downloads.sourceforge.net/freeglut/' \
                   'freeglut-$version.tar.gz'
        self.depends = ['glu', 'mesa']
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]
