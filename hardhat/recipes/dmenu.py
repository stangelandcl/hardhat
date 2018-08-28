from .base import GnuRecipe


class DMenuRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DMenuRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fe615a5c3607061e2106700862e82ac6' \
                      '2a9fa1e6a7ac3d616a9c76106476db61'
        self.name = 'dmenu'
        self.version = '4.8'
        self.depends = ['freetype', 'xorg-libs']
        self.url = 'https://dl.suckless.org/tools/dmenu-$version.tar.gz'
        self.compile_args += [
            'PREFIX=%s' % self.prefix_dir,
            'FREETYPEINC=%s/include/freetype2' % self.prefix_dir]
        self.install_args += ['PREFIX=%s' % self.prefix_dir]
