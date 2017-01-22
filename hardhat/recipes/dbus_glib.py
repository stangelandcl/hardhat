from .base import GnuRecipe


class DbusGlibRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DbusGlibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'bfc1f1a82bfc3ec3ecafe04d0e87bab7' \
                      'e999f50dce4f4a34d0b89caf6bd821f6'

        self.name = 'dbus-glib'
        self.version = '0.104'
        self.depends = ['dbus', 'glib']
        self.url = 'http://dbus.freedesktop.org/releases/dbus-glib/' \
                   'dbus-glib-$version.tar.gz'
