from .base import GnuRecipe


class DbusRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DbusRecipe, self).__init__(*args, **kwargs)

        self.name = 'dbus'
        self.version = '1.13.4'
        self.depends = ['xorg-libs']
        self.url = 'http://dbus.freedesktop.org/releases/dbus/' \
                   'dbus-$version.tar.gz'

        self.configure_args += ['--disable-doxygen-docs',
                                '--disable-xml-docs',
                                '--disable-systemd',
                                '--without-systemdsystemunitdir']

    def install(self):
        super(DbusRecipe, self).install()

        self.install_args = ['dbus-uuidgen', '--ensure']
        super(DbusRecipe, self).install()
