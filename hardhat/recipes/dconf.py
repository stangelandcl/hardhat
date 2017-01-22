from .base import GnuRecipe


class DconfRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DconfRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4373e0ced1f4d7d68d518038796c0736' \
                      '96280e22957babb29feb0267c630fec2'

        self.name = 'dconf'
        self.version = '0.24.0'
        self.depends = ['dbus', 'glib']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/dconf/' \
                   '%s/dconf-$version.tar.xz' % self.short_version

        self.configure_args += ['--enable-man=no']
