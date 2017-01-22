from .base import GnuRecipe


class DbusRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DbusRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fa207530d694706e33378c87e65b2b43' \
                      '04eb99fff71fc6d6caa6f70591b9afd5'

        self.name = 'dbus'
        self.version = '1.11.8'
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
