from .base import GnuRecipe


class FlacRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FlacRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4773c0099dba767d963fd92143263be3' \
                      '38c48702172e8754b9bc5103efe1c56c'

        self.name = 'flac'
        self.depends = ['doxygen', 'libogg', 'yasm']
        self.version = '1.3.1'
        self.url = 'http://downloads.xiph.org/releases/flac/' \
                   'flac-$version.tar.xz'

        self.configure_args += ['--disable-thorough-tests']
        self.environment_strip_lto()
