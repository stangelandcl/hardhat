from .base import GnuRecipe


class GudevRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GudevRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a2e77faced0c66d7498403adefcc0707' \
                      '105e03db71a2b2abd620025b86347c18'

        self.name = 'gudev'
        self.version = '230'
        self.depends = ['glib', 'gobject-introspection', 'gtk-doc']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/libgudev/' \
                   '$version/libgudev-$version.tar.xz'
        self.configure_args += ['--enable-gtk-doc']
