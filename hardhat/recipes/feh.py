from .base import GnuRecipe


class FehRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FehRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '074f8527a17fc5add70018a7f3887d78' \
                      'd5bdf545611636b88641f27e9e844795'
                
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
