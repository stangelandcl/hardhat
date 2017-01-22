from .base import GnuRecipe


class GimpRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GimpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '39dd2247c678deaf5cc664397d3c6bd4' \
                      'fb910d3472290fd54b52b441b5815441'

        self.name = 'gimp'
        self.version = '2.8.18'
        self.depends = ['babl', 'gegl', 'gtk2']
        self.url = 'https://download.gimp.org/mirror/pub/gimp/v%s/' \
                   'gimp-$version.tar.bz2' % self.short_version
