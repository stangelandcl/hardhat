from .base import GnuRecipe


class GtkSourceViewRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GtkSourceViewRecipe, self).__init__(*args, **kwargs)
        self.name = 'gtksourceview'
        self.version = '3.24.8'
        short_version = '.'.join(self.version.split('.')[:2])
        self.depends = ['gobject-instrospection', 'gtk3', 'vala']

        self.url = 'http://ftp.gnome.org/pub/gnome/sources/gtksourceview/' \
                   '%s/gtksourceview-$version.tar.xz' % (short_version)
        self.configure_args += [
            '--enable-vala=no',
            '--enable-valgrind=no']
