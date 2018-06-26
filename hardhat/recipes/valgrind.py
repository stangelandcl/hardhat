from .base import GnuRecipe


class ValgrindRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ValgrindRecipe, self).__init__(*args, **kwargs)
        self.name = 'valgrind'
        self.version = '3.13.0'
        self.url = 'http://valgrind.org/downloads/valgrind-$version.tar.bz2'

        self.environment_strip_lto()
