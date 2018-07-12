from .base import GnuRecipe


class DbusRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DbusRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8a8f0b986ac6214da9707da521bea9f4' \
                      '9f09610083c71fdc8eddf8b4c54f384b'
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
