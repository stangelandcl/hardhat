from .base import GnuRecipe


class EvinceRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(EvinceRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0955d22d85c9f6d322b6cbb464f1cc4c' \
                      '352db619017ec95dad4cc5c3440f73e1'
        self.name = 'evince'
        self.version = '3.28.2'
        self.version_regex = r'(?P<version>\d+\.\d+)'
        self.version_url = 'http://ftp.gnome.org/pub/gnome/sources/evince/'
        self.depends = ['adwaita-icon-theme',
                        'gsettings-desktop-schemas',
#                        'gspell',
                        'gtk3',
                        'itstool',
                        'libsecret',
                        'libspectre',
                        'libxml2',
                        'nautilus',
                        'poppler']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/evince/' \
                   '%s/evince-$version.tar.xz' % self.short_version
