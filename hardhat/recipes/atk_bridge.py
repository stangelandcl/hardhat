from .base import GnuRecipe


class AtkBridgeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AtkBridgeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2358a794e918e8f47ce0c7370eee8fc8' \
                      'a6207ff1afe976ec9ff547a03277bf8e'


        self.name = 'atk-bridge'
        self.depends = ['atk', 'atspi']
        self.version = '2.20.1'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/at-spi2-atk/%s/' \
                   'at-spi2-atk-$version.tar.xz' % short_version
