from .base import GnuRecipe


class ValgrindRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ValgrindRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd76680ef03f00cd5e970bbdcd4e57fb1' \
                      'f6df7d2e2c071635ef2be74790190c3b'

        self.name = 'valgrind'
        self.version = '3.13.0'
        self.version_url = 'http://valgrind.org/downloads/current.html'
        self.url = 'ftp://sourceware.org/pub/valgrind/valgrind-$version.tar.bz2'
        self.environment_strip_lto()
