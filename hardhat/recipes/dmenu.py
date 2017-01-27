from .base import GnuRecipe


class DMenuRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DMenuRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd633309a413f94e791eb9340fad71b87' \
                      'b6ea56f04ce7ac20538b3d05ff873cd6'

        self.name = 'dmenu'
        self.version = '5cd66e2c6ca6a82e59927d495498fa6e478594d6'
        self.depends = ['freetype']
        self.url = 'http://git.suckless.org/dmenu/snapshot/dmenu-$version.tar.gz'
        self.compile_args += [
            'PREFIX=%s' % self.prefix_dir,
            'FREETYPEINC=%s/include/freetype2' % self.prefix_dir]
        self.install_args += ['PREFIX=%s' % self.prefix_dir]
