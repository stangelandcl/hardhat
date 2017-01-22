from .base import GnuRecipe


class OpenBoxRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpenBoxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8b4ac0760018c77c0044fab06a4f0c51' \
                      '0ba87eae934d9983b10878483bde7ef7'

        self.name = 'openbox'
        self.version = '3.6.1'
        self.depends = ['dbus', 'imlib2', 'librsvg', 'pango',
                        'python2-pyxdg',
                        'startup-notification',
                        'xorg-libs']
        self.url = 'http://openbox.org/dist/openbox/openbox-$version.tar.gz'
