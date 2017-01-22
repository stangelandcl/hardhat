from .base import GnuRecipe


class GtkHtmlRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GtkHtmlRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ca3b6424fb2c7ac5d9cb8fdafb69318f' \
                      'a2e825c9cf6ed17d1e38d9b29e5606c3'

        self.name = 'gtkhtml'
        self.version = '4.10.0'
        self.depends = ['enchant', 'gsettings-desktop-schemas', 'gtk3',
                        'iso-codes']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/gtkhtml/%s/' \
                   'gtkhtml-$version.tar.xz' % self.short_version
