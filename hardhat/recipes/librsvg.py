from .base import GnuRecipe


class LibrsvgRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibrsvgRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd48bcf6b03fa98f07df10332fb49d8c0' \
                      '10786ddca6ab34cbba217684f533ff2e'

        self.name = 'librsvg'
        self.depends = ['cairo', 'gdk-pixbuf', 'libcroco', 'pango']
        self.version = '2.40.16'
        self.url = 'https://download.gnome.org/sources/librsvg/2.40/' \
                   'librsvg-$version.tar.xz'
