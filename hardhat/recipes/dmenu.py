from .base import GnuRecipe


class DMenuRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DMenuRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '364f2eadd5b098f47cce23f6ad5a5161' \
                      '34af508a461e4d83cb27d73f70303d3d'

        self.name = 'dmenu'
        self.version = '5cd66e2c6ca6a82e59927d495498fa6e478594d6'
        self.depends = ['freetype']
        self.url = 'http://git.suckless.org/dmenu/snapshot/dmenu-$version.tar.gz'
        self.compile_args += [
            'PREFIX=%s' % self.prefix_dir,
            'FREETYPEINC=%s/include/freetype2' % self.prefix_dir]
        self.install_args += ['PREFIX=%s' % self.prefix_dir]
