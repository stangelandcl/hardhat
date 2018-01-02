from .base import GnuRecipe


class Exiv2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Exiv2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c75e3c4a0811bf700d92c82319373b7a' \
                      '825a2331c12b8b37d41eb58e4f18eafb'
        self.name = 'exiv2'
        self.version = '0.26'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools']
        self.url = 'http://www.exiv2.org/builds/exiv2-$version-trunk.tar.gz'
