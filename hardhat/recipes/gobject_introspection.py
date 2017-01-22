from .base import GnuRecipe


class GObjectIntrospectionRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GObjectIntrospectionRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fa275aaccdbfc91ec0bc9a6fd0562051' \
                      'acdba731e7d584b64a277fec60e75877'

        self.name = 'gobject-introspection'
        self.version = '1.48.0'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/' \
                   'gobject-introspection/%s/' \
                   'gobject-introspection-$version.tar.xz' % short_version
