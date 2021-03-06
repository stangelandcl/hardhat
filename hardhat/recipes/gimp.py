from .base import GnuRecipe


class GimpRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GimpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9187a35cc52b110d78124d7b27b68a68' \
                      'ade14a794c2721314bac6134d2a5638a'

        self.name = 'gimp'
        self.version = '2.8.22'
        self.depends = ['babl', 'python2-pygtk', 'gegl', 'gtk2']
        self.url = 'https://download.gimp.org/mirror/pub/gimp/v%s/' \
                   'gimp-$version.tar.bz2' % self.short_version

    def patch(self):
        self.log_dir('patch', self.directory, 'patch gegl-0.2 to gegl-0.3')
        # Patches from BLFS
        args = [["sed", "-i", "'/gegl/s/2/3/'", "./configure"],
                ["sed", "-i", "'70,75 d'", "./app/core/gimpparamspecs-duplicate.c"]]
        for arg in args:
            self.run_exe(arg, self.directory, self.environment)
