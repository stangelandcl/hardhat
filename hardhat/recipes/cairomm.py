from .base import GnuRecipe


class CairommRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CairommRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8db629f44378cac62b4931f725520334' \
                      '024e62c1951c4396682f1add63c1e3d1'
        self.name = 'cairomm'
        self.version = '1.15.5'
        self.depends = ['cairo', 'fontconfig', 'glib', 'libsigc++', 'xorg-libs']
        self.url = 'http://cairographics.org/releases/cairomm-$version.tar.gz'
