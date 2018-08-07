from .base import GnuRecipe


class PangoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PangoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '90af1beaa7bf9e4c52db29ec251ec4fd' \
                      '0a8f2cc185d521ad1f88d01b3a6a17e3'

        self.name = 'pango'
        self.depends = ['cairo', 'fontconfig', 'glib', 'harfbuzz']
        self.version = '1.40.14'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/$name/' \
                   '%s/$name-$version.tar.xz' % short_version
