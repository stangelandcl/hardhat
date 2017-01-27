from .base import GnuRecipe


class DMenuRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DMenuRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9755d8bcff0d65779009d4ed31072f2e' \
                      '88e9a2c2f86d01d8b6079ad75f559503'
        self.name = 'dmenu'
        self.version = '5cd66e2c6ca6a82e59927d495498fa6e478594d6'
        self.depends = ['freetype']
        self.url = 'http://git.suckless.org/dmenu/snapshot/dmenu-$version.tar.gz'
        self.compile_args += [
            'PREFIX=%s' % self.prefix_dir,
            'FREETYPEINC=%s/include/freetype2' % self.prefix_dir]
        self.install_args += ['PREFIX=%s' % self.prefix_dir]
