from .base import GnuRecipe


class GeglRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GeglRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '06ca9e67a59da026eb941b9d323269d7' \
                      'c19a922f1e478acdd3791a0eef8b229b'

        self.name = 'gegl'
        self.version = '0.3.8'
        self.depends = ['babl', 'json-glib']
        self.url = 'http://download.gimp.org/pub/gegl/0.3/' \
                   'gegl-$version.tar.bz2'
