from .base import GnuRecipe


class PangoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PangoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'abba8b5ce728520c3a0f1535eab19eac' \
                      '3c14aeef7faa5aded90017ceac2711d3'
        self.name = 'pango'
        self.depends = ['cairo', 'fontconfig', 'glib', 'harfbuzz']
        self.version = '1.40.3'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/$name/' \
                   '%s/$name-$version.tar.xz' % short_version
