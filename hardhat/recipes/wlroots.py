import os
from .base import GnuRecipe
from ..version import extension_regex


class WlRootsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(WlRootsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ab257be32910b1386204c76873ff81f8' \
                      '8cf8d98178eab628f89a71811fb12ea5'
        self.name = 'wlroots'
        self.depends = ['gdk-pixbuf',
                        'json-c', 'libcap', 'libinput', 'linux-pam',
                        'libxkbcommon', 'mesa', 'meson', 'pango',
                        'pcre', 'pixman', 'pkgconfig', 'util-linux',
                        'wayland', 'wayland-protocols', 'xorg-libs']
        # Plus install a specific driver for better performance
        # see recipes/x11/drivers for a list
        # Also install the synaptics driver in that directory
        # for laptop touchpad support
        self.environment['CFLAGS'] += \
            ' -Wno-error=unused-function -Wno-error=return-type -Wno-error=unused-variable'
        self.version = '2f484537181c515082b632f9d575613abda72a48'
        self.version_regex = r'(?P<version>\d+\.\d+(-rc\d+)?)' \
            + extension_regex
        self.version_url = 'https://github.com/SirCmpwn/wlroots/releases'
        self.url = 'https://github.com/swaywm/wlroots/archive/$version.tar.gz'
        self.configure_args = ['meson', 'build',
                               '--prefix %s' % self.prefix_dir,
                               '--buildtype', 'release']
        self.compile_args = ['ninja', '-C', 'build']
        self.install_args = ['ninja', '-C', 'build', 'install']
