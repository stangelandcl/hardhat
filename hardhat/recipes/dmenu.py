from .base import GnuRecipe


class DMenuRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DMenuRecipe, self).__init__(*args, **kwargs)
        self.sha256 = None  # hash changes every time

        self.name = 'dmenu'
        self.version = 'f428f3e01a4ced5b1df07ddf913bb022692f8035'
        self.depends = ['freetype', 'xorg-libs']
        self.url = 'http://git.suckless.org/dmenu/snapshot/dmenu-$version.tar.gz'
        self.compile_args += [
            'PREFIX=%s' % self.prefix_dir,
            'FREETYPEINC=%s/include/freetype2' % self.prefix_dir]
        self.install_args += ['PREFIX=%s' % self.prefix_dir]
