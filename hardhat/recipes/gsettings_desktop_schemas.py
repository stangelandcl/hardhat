from .base import GnuRecipe


class GsettingsDesktopSchemasRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GsettingsDesktopSchemasRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0f06c7ba34c3a99e4d58b10889496133' \
                      'c9aaad6698ea2d8405d481c7f1a7eae1'

        self.name = 'gsettings-desktop-schemas'
        self.version = '3.22.0'
        self.depends = ['glib']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/' \
                   'gsettings-desktop-schemas/%s/' \
                   'gsettings-desktop-schemas-$version.tar.xz' \
                   % self.short_version
