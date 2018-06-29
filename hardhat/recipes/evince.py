from .base import GnuRecipe


class EvinceRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(EvinceRecipe, self).__init__(*args, **kwargs)
        self.name = 'evince'
        self.version = '3.28'
        self.version_regex = r'(?P<version>\d+\.\d+(\.\d+)?)'
        self.version_url = 'http://ftp.gnome.org/pub/gnome/sources/evince/'
        self.depends = ['adwaita-icon-theme',
                        'gsettings-desktop-schemas',
                        'gtk3',
                        'itstool',
                        'libsecret',
                        'libspectre',
                        'libxml2',
                        'nautilus',
                        'poppler']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/evince/' \
                   '%s/evince-$version.tar.xz' % self.short_version

