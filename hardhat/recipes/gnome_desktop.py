from .base import GnuRecipe


class GnomeDesktopRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GnomeDesktopRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ddd46d022de137543a71f50c7392b32f' \
                      '9b98d5d3f2b53040b35f5802de2e7b56'

        self.description = 'Gnome Desktop'
        self.name = 'gnome-desktop'
        self.version = '3.18.2'
        self.depends = ['gobject-introspection',
                        'gsettings-desktop-schemas', 'gtk3', 'iso-codes',
                        'itstool', 'xkeyboard-config']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/gnome-desktop/' \
                   '$short_version/gnome-desktop-$version.tar.xz'
