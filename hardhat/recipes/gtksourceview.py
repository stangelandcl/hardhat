from .base import GnuRecipe


class GtkSourceViewRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GtkSourceViewRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5d2820e1f5c5d063ef6574d2bc71268b' \
                      '066e74efa2571ef1031210164e51e37d'

        self.name = 'gtksourceview'
        self.version = '3.16.2'
        short_version = '.'.join(self.version.split('.')[:2])
        self.depends = ['gobject-instrospection', 'gtk3']

        self.url = 'http://ftp.gnome.org/pub/gnome/sources/gtksourceview/' \
                   '%s/gtksourceview-$version.tar.xz' % (short_version)
