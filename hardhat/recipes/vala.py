from .base import GnuRecipe


class ValaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ValaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6b17bd339414563ebc51f64b0b837919' \
                      'ea7552d8a8ffa71cdc837d25c9696b83'

        self.name = 'vala'
        self.version = '0.34.4'
        self.depends = ['dbus', 'glib', 'libxslt']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/vala/%s/' \
                   'vala-$version.tar.xz' % self.short_version
