from .base import GnuRecipe


class FlacRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FlacRecipe, self).__init__(*args, **kwargs)
        self.name = 'flac'
        self.depends = ['doxygen', 'libogg', 'yasm']
        self.version = '1.3.2'
        self.url = 'http://downloads.xiph.org/releases/flac/' \
                   'flac-$version.tar.xz'

        self.configure_args += ['--disable-thorough-tests']
        self.environment_strip_lto()
