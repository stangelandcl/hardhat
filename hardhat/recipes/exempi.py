from .base import GnuRecipe


class ExempiRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ExempiRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '406185feb88e84ea1d4b4251370be299' \
                      '1205790d7113a7e28e192ff46a4f221e'

        self.name = 'exempi'
        self.depends = ['boost']
        self.version = '2.4.5'
        self.url = 'http://libopenraw.freedesktop.org/download/' \
                   'exempi-$version.tar.bz2'
        self.configure_args += ['--with-boost=%s' % self.prefix_dir,
                                '--enable-unittest=no']
