from .base import GnuRecipe


class ValgrindRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ValgrindRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '67ca4395b2527247780f36148b084f57' \
                      '43a68ab0c850cb43e4a5b4b012cf76a1'

        self.name = 'valgrind'
        self.version = '3.12.0'
        self.url = 'http://valgrind.org/downloads/valgrind-$version.tar.bz2'

        self.environment_strip_lto()
