import os
from .base import GnuRecipe
from hardhat.util import patch


class Gtk3Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Gtk3Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e7e3aaf54a54dd1c1ca0588939254abe' \
                      '31329e0bcd280a12290d5306b41ea03f'

        self.name = 'gtk3'
        self.version = '3.20.4'
        short_version = '.'.join(self.version.split('.')[:2])
        self.depends = ['atk', 'atk-bridge', 'gdk-pixbuf', 'glib',
                        'libepoxy', 'libxkbcommon', 'pango',
                        'wayland', 'wayland-protocols',
                        'xorg-libs']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/gtk+/' \
                   '%s/gtk+-$version.tar.xz' % (short_version)
        self.configure_args += ['--with-x',
                                '--enable-xkb',
                                '--enable-xrandr',
                                '--enable-wayland-backend',
                                '--enable-x11-backend']

    def patch(self):
        self.log_dir('patch', self.directory, 'disable pk-gtk-module')

        src = 'g_str_equal (name, "atk-bridge"))'
        dst = 'g_str_equal (name, "pk-gtk-module") ||\n' \
              '      g_str_equal (name, "atk-bridge"))'

        filename = os.path.join(self.directory, 'gtk', 'gtkmodules.c')
        patch(filename, src, dst)
