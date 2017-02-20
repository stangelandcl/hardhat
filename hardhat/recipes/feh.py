from .base import GnuRecipe


class FehRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FehRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '34be64648f8ada0bb666e226beac601f' \
                      '972b695c9cfa73339305124dbfcbc525'
        self.name = 'feh'
        self.version = '2.18.2'
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
