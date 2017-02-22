from .base import GnuRecipe


class ChromiumRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ChromiumRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e81bd3140d9c84dfee04d9a94686dfe6' \
                      'a20ae79475d84f17154c5536dcb81a58'

        self.name = 'chromium'
        self.version = '55.0.2883.87'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+\.\d+)'
        self.depends = [
            'alsa-lib',
            'cups',
            'desktop-file-utils',
            'dbus',
            'flac',
            'gtk2',
            'hicolor-icon-theme',
            'libevent',
            'libexif',
            'mit-kerberos',
            'mesa',
            'ninja',
            'nss',
            'pciutils',
            'python2',
            'usbutils',
            'xorg-libs',
            'yasm',
        ]
        self.url = 'https://commondatastorage.googleapis.com/' \
                   'chromium-browser-official/chromium-$version.tar.xz'
