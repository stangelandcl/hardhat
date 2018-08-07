from .base import GnuRecipe


class EvinceRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(EvinceRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'caecbd48feed1ba88aadad0713240232' \
                      '17c644f86e6c99dc14af5c7ebb5d0423'

        self.name = 'evince'
        self.version = '3.29.90'
        self.version_regex = r'(?P<version>\d+\.\d+)'
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
