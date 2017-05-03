from .base import GnuRecipe


class GluRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GluRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1f7ad0d379a722fcbd303aa5650c6d7d' \
                      '5544fde83196b42a73d1193568a4df12'

        self.name = 'glu'
        self.version = '9.0.0'
        self.depends = ['mesa']
        self.url = 'ftp://ftp.freedesktop.org/pub/mesa/glu/' \
                   'glu-$version.tar.bz2'
