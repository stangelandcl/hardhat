from .base import GnuRecipe


class JemallocRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JemallocRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a7aea63e9718d2f1adf81d87e3df3cb1' \
                      'b58deb86fc77bad5d702c4c59687b033'

        self.name = 'jemalloc'
        self.version = '4.4.0'
        self.version_url = 'https://github.com/jemalloc/jemalloc/releases'
        self.url = 'https://github.com/jemalloc/jemalloc/releases/download/' \
                   '$version/jemalloc-$version.tar.bz2'
