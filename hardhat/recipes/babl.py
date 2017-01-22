from .base import GnuRecipe


class BablRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BablRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '483a495bc9fa68be624e27e72d2144eb' \
                      'fcbbf63e061eb986db1fb82b04b6fbf9'

        self.name = 'babl'
        self.version = '0.1.18'
        self.depends = ['gobject-introspection']
        self.url = 'http://download.gimp.org/pub/babl/0.1/babl-$version.tar.bz2'
