from .base import GnuRecipe


class FehRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FehRecipe, self).__init__(*args, **kwargs)
        self.name = 'feh'
        self.version = '2.26.4'
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
