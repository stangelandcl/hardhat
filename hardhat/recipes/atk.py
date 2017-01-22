from .base import GnuRecipe


class AtkRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AtkRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '493a50f6c4a025f588d380a551ec277e' \
                      '070b28a82e63ef8e3c06b3ee7c1238f0'

        self.name = 'atk'
        self.version = '2.20.0'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/atk/' \
                   '%s/atk-$version.tar.xz' % (short_version)
