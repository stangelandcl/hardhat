from .base import GnuRecipe


class AtspiRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AtspiRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6ed858e781f5aa9a9662b3beb5ef82f7' \
                      '33dac040afc8255d85dffd2097f16900'

        self.name = 'atspi'
        self.depends = ['dbus', 'gettext', 'intltool']
        self.version = '2.20.1'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/at-spi2-core/' \
                   '%s/at-spi2-core-$version.tar.xz' % short_version
