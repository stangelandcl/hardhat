from .base import GnuRecipe


class GspellRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GspellRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '819a1d23c7603000e73f5e738bdd2843' \
                      '42e0cd345fb0c7650999c31ec741bbe5'
        self.name = 'gspell'
        self.depends = ['enchant', 'gtk3']
        self.version = '1.8.1'
        self.version_regex = r'(?P<version>\d+\.\d+(\.\d+)?)'
        self.version_url = 'https://download.gnome.org/sources/gspell'
        self.url = 'https://download.gnome.org/sources/gspell/%s/' \
                   'gspell-$version.tar.xz' % ('.'.join(self.version.split('.')[:2]))
