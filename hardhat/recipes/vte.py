from .base import GnuRecipe


class Vte28Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Vte28Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '86cf0b81aa023fa93ed415653d51c967' \
                      '67f20b2d7334c893caba71e42654b0ae'

        self.name = 'vte28'
        self.version = '0.28.2'
        self.depends = ['gtk2', 'gobject-introspection', 'gtk-doc']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/vte/%s/' \
                   'vte-$version.tar.xz' % self.short_version
        self.configure_args += ['--libexecdir=%s/lib/vte' % self.prefix_dir]


class Vte40Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Vte40Recipe, self).__init__(*args, **kwargs)
        self.name = 'vte40'
        self.version = '0.46.1'
        self.depends = ['gtk3', 'gnutls', 'gobject-introspection',
                        'gtk-doc', 'libxml2', 'pcre2', 'vala']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/vte/%s/' \
                   'vte-$version.tar.xz' % self.short_version
        self.configure_args += ['--libexecdir=%s/lib/vte' % self.prefix_dir]
