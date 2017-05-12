from .base import GnuRecipe


class GtkSourceViewRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GtkSourceViewRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '717b6fe884ff9f25158bdc36f463790c' \
                      '608ada9f5e2e6f4dc7f1467c83711c25'
        self.name = 'gtksourceview'
        self.version = '3.24.1'
        short_version = '.'.join(self.version.split('.')[:2])
        self.depends = ['gobject-instrospection', 'gtk3', 'vala']

        self.url = 'http://ftp.gnome.org/pub/gnome/sources/gtksourceview/' \
                   '%s/gtksourceview-$version.tar.xz' % (short_version)
        self.configure_args += [
            '--enable-vala=no',
            '--enable-valgrind=no']
