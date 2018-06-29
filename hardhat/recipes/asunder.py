from .base import GnuRecipe


class AsunderRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AsunderRecipe, self).__init__(*args, **kwargs)
        self.name = 'asunder'
        self.version = '2.9.3'
        self.depends = ['flac', 'gtk2', 'lame', 'libcanberra', 'libcddb']
        self.url = 'http://littlesvr.ca/asunder/releases/' \
                   'asunder-$version.tar.bz2'
