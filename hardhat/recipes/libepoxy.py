from .base import GnuRecipe


class LibEpoxyRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibEpoxyRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1d8668b0a259c709899e1c4bab62d756' \
                      'd9002d546ce4f59c9665e2fc5f001a64'

        self.name = 'libepoxy'
        self.version = '1.3.1'
        self.depends = ['mesa']
        self.url = 'https://github.com/anholt/libepoxy/releases/download/' \
                   'v$version/libepoxy-$version.tar.bz2'
