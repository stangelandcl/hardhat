from .base import GnuRecipe


class Gtk2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Gtk2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '0d15cec3b6d55c60eac205b1f3ba81a1' \
                      'ed4eadd9d0f8e7c508bc7065d0c4ca50'

        self.name = 'gtk2'
        self.version = '2.24.30'
        short_version = '.'.join(self.version.split('.')[:2])
        self.depends = ['atk', 'gdk-pixbuf',
                        'gobject-introspection',
                        'gtk-doc',
                        'hicolor-icon-theme', 'pango']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/gtk+/' \
                   '%s/gtk+-$version.tar.xz' % (short_version)
