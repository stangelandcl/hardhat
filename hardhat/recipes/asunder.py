from .base import GnuRecipe


class AsunderRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AsunderRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e69698f9524e443ac564b5d4b2df135e' \
                      'd7e5b2f94d6b3cabeae5bb2a3c828914'

        self.name = 'asunder'
        self.version = '2.7'
        self.depends = ['flac', 'gtk2', 'lame', 'libcanberra', 'libcddb']
        self.url = 'http://littlesvr.ca/asunder/releases/' \
                   'asunder-$version.tar.bz2'
