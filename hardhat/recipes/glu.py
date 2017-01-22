from .base import GnuRecipe


class GluRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GluRecipe, self).__init__(*args, **kwargs)
        self.sha256 = None
        self.name = 'glu'
        self.version = '9.0.0'
        self.depends = ['mesa']
        self.url = 'ftp://ftp.freedesktop.org/pub/mesa/glu/' \
                   'glu-$version.tar.bz2'
