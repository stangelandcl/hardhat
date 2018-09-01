import os
from .base import GnuRecipe
from hardhat.util import patch


class Gtk3Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Gtk3Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a1a4a5c12703d4e1ccda28333b87ff46' \
                      '2741dc365131fbc94c218ae81d9a6567'
        self.name = 'gtk3'
        self.version = '3.22.30'
        self.depends = ['atk', 'atk-bridge', 'gdk-pixbuf', 'glib',
                        'libepoxy', 'libxkbcommon', 'pango',
                        'shared-mime-info',
                        'wayland', 'wayland-protocols',
                        'xorg-libs']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/gtk+/' \
                   '%s/gtk+-$version.tar.xz' % self.short_version
        self.configure_args += ['--with-x',
                                '--enable-xkb',
                                '--enable-xrandr',
                                '--enable-wayland-backend',
                                '--enable-x11-backend']

    def patch(self):
        self.log_dir('patch', self.directory, 'disable pk-gtk-module')

#        src = 'g_str_equal (name, "atk-bridge"))'
#        dst = 'g_str_equal (name, "pk-gtk-module") ||\n' \
#              '      g_str_equal (name, "atk-bridge"))'

#        filename = os.path.join(self.directory, 'gtk', 'gtkmodules.c')
#        patch(filename, src, dst)
