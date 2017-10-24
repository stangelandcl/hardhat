from .base import Mingw64BaseRecipe


class Mingw64LibCsvRecipe(Mingw64BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Mingw64LibCsvRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd9c0431cb803ceb9896ce74f683e6e5a' \
                      '0954e96ae1d9e4028d6e0f967bebd7e4'

        self.name = 'mingw64-libcsv'
        self.version = '3.0.3'
        self.url = 'http://downloads.sourceforge.net/project/libcsv/libcsv/' \
                   'libcsv-$version/libcsv-$version.tar.gz'
