from .base import GnuRecipe


class ValaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ValaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c7ff0480779b2d78d6ff78f5fd165b3b' \
                      'a972e4fa9e9da1b411ff4375a78c6a7b'
        self.name = 'vala'
        self.version = '0.40.9'
        self.depends = ['dbus', 'glib', 'libxslt']
        self.version_regex = 'vala\-(?P<version>\d+\.\d+\.\d+)\.tar'
        self.version_url = 'https://wiki.gnome.org/Projects/Vala/Release'
        self.url = 'http://download.gnome.org/sources/vala/%s/' \
                   'vala-$version.tar.xz' % self.short_version
        self.configure_strip_cross_compile()
