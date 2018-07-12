from .base import GnuRecipe


class GObjectIntrospectionRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GObjectIntrospectionRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5b2875ccff99ff7baab63a34b67f8c92' \
                      '0def240e178ff50add809e267d9ea24b'
        self.name = 'gobject-introspection'
        self.version = '1.56.1'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/' \
                   'gobject-introspection/%s/' \
                   'gobject-introspection-$version.tar.xz' % short_version
