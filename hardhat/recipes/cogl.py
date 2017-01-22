from .base import GnuRecipe


class CoglRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CoglRecipe, self).__init__(*args, **kwargs)
        self.sha256 = None

        self.name = 'cogl'
        self.version = '1.22.0'
        self.depends = ['gdk-pixbuf', 'gobject-introspection', 'mesa', 'pango']
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'ftp://ftp.gnome.org/pub/gnome/sources/cogl/%s/' \
                   'cogl-$version.tar.xz' % short_version
