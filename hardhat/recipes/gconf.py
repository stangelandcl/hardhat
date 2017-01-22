from .base import GnuRecipe


class GconfRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GconfRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1912b91803ab09a5eed34d364bf09fe3' \
                      'a2a9c96751fde03a4e0cfa51a04d784c'

        self.name = 'gconf'
        self.version = '3.2.6'
        short_version = '.'.join(self.version.split('.')[:2])
        self.depends = ['dbus-glib', 'gobject-introspection', 'libxml2']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/GConf/' \
                   '%s/GConf-$version.tar.xz' % short_version
        self.configure_args += ['--disable-orbit']
