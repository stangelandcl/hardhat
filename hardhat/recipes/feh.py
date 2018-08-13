from .base import GnuRecipe


class FehRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FehRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6ec338f80c3f4c30d715f44780f1a09e' \
                      'bfbb99e92a1bb43316428744a839f383'

        self.name = 'feh'
        self.version = '2.27.1'
        self.depends = ['curl',
                        'imagemagick',
                        'imlib2',
                        'libexif',
                        'libjpeg-turbo',
                        'libpng']
        self.url = 'http://feh.finalrewind.org/feh-$version.tar.bz2'
        self.compile_args += ['PREFIX=%s' % self.prefix_dir]
        self.install_args += ['PREFIX=%s' % self.prefix_dir]

    def configure(self):
        pass
