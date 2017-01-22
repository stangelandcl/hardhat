from .base import GnuRecipe


class FirefoxRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FirefoxRecipe, self).__init__(*args, **kwargs)
        self.name = 'firefox'
        self.version = '50.1.0'
        self.version_regex = r'(?P<version>\d+\.\d+(\.\d+)*)'
        self.version_url = 'https://ftp.mozilla.org/pub/mozilla.org/firefox/' \
                           'releases/'
        self.depends = ['alsa-lib',
                        'autoconf',
                        'gtk3',
                        'nss',
                        'unzip',
                        'yasm',
                        'zip'
                        ]
        self.url = 'https://ftp.mozilla.org/pub/mozilla.org/firefox/' \
                   'releases/$version/source/firefox-$version.source.tar.xz'
