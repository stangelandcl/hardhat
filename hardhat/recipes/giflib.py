from .base import GnuRecipe



class GifLibRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GifLibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'df27ec3ff24671f80b29e6ab1c497105' \
                      '9c14ac3db95406884fc26574631ba8d5'
        self.name = 'giflib'
        self.version = '5.1.4'
        self.url = 'http://downloads.sourceforge.net/project/giflib/' \
                   'giflib-$version.tar.bz2'
        self.configure_args += ['have_xmlto=no']
