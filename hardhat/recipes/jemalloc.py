from .base import GnuRecipe


class JemallocRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JemallocRecipe, self).__init__(*args, **kwargs)
        self.name = 'jemalloc'
        self.version = '5.1.0'
        self.version_url = 'https://github.com/jemalloc/jemalloc/releases'
        self.url = 'https://github.com/jemalloc/jemalloc/releases/download/' \
                   '$version/jemalloc-$version.tar.bz2'
