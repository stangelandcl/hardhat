from .base import GnuRecipe
from ..version import extension_regex


class WlcRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(WlcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '47e9b756d3fd621df913a6fbc9378c47' \
                      'aa8f9c3be7c2228a657a2411a7211979'

        self.name = 'wlc'
        self.depends = ['doxygen',
                        'eudev',
                        'libdrm',
                        'libinput',
                        'libxcb',
                        'libxkbcommon',
                        'mesa',
                        'pixman',
                        'wayland',
                        'wayland-protocols',
                        'xcb-util-image',
                        'xcb-util-wm',
                        'xorg-libs']
        self.version = '0.0.7'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)' \
            + extension_regex
        self.version_url = 'https://github.com/Cloudef/wlc/releases'
        self.url = 'https://github.com/Cloudef/wlc/releases/download/' \
                   'v$version/wlc-$version.tar.bz2'
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]
