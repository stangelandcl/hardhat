from .base import GnuRecipe


class DbusGlibRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DbusGlibRecipe, self).__init__(*args, **kwargs)

        self.name = 'dbus-glib'
        self.version = '0.110'
        self.depends = ['dbus', 'glib']
        self.url = 'http://dbus.freedesktop.org/releases/dbus-glib/' \
                   'dbus-glib-$version.tar.gz'
