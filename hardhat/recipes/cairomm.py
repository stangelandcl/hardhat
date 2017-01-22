from .base import GnuRecipe


class CairommRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CairommRecipe, self).__init__(*args, **kwargs)
        self.sha256 = None

        self.name = 'cairomm'
        self.version = '1.12.0'
        self.depends = ['cairo', 'fontconfig', 'glib', 'libsigc++', 'xorg-libs']
        self.url = 'http://cairographics.org/releases/cairomm-$version.tar.gz'
