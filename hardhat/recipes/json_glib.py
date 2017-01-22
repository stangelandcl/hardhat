from .base import GnuRecipe


class JsonGlibRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JsonGlibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '99d6dfbe49c08fd7529f1fe8dcb1893b' \
                      '810a1bb222f1e7b65f41507658b8a7d3'

        self.name = 'json-glib'
        self.version = '1.2.0'
        self.depends = ['glib', 'gobject-introspection', 'gtk-doc']
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'ftp://ftp.gnome.org/pub/gnome/sources/$name/%s/' \
                   '$name-$version.tar.xz' % short_version
