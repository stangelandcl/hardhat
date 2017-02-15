from .base import GnuRecipe


class NautilusRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NautilusRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '60a927c0522b4cced9d8f62baed2ee5e' \
                      '2fd4305be4523eb5bc44805971a6cc15'

        self.description = 'File manager'
        self.name = 'nautilus'
        self.version = '3.18.5'
        self.depends = ['exempi', 'gnome-desktop', 'libexif', 'libnotify']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/nautilus/' \
                   '$short_version/nautilus-$version.tar.xz'
        self.configure_args += ['--disable-tracker',
                                '--disable-packagekit']
