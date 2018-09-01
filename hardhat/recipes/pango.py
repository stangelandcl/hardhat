from .base import GnuRecipe


class PangoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PangoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1d2b74cd63e8bd41961f2f8d952355aa' \
                      '0f9be6002b52c8aa7699d9f5da597c9d'

        self.name = 'pango'
        self.depends = ['cairo', 'fontconfig', 'glib', 'harfbuzz']
        self.version = '1.42.4'
        self.version_regex = '(?P<version>\d+\.\d+)'
        self.version_url = 'http://ftp.gnome.org/pub/GNOME/sources/pango/'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/$name/' \
                   '%s/$name-$version.tar.xz' % short_version
