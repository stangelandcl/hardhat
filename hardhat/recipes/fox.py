from .base import GnuRecipe


class FoxRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FoxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '960f16a8a69d41468f841039e83c2f58' \
                      'f3cb32622fc283a69f20381abb355219'

        self.description = 'C++ GUI toolkit'
        self.name = 'fox'
        self.version = '1.6.54'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = [
            'bzip2',
            'freetype',
            'glu',
            'libjpeg-turbo',
            'libpng',
            'libtiff',
            'mesa',
            'xorg-libs',
            'zlib'
            ]
        self.url = 'http://ftp.fox-toolkit.org/pub/fox-$version.tar.gz'
        self.environment['CPPFLAGS'] += \
            ' -I%s/include/freetype2' % self.prefix_dir
#        self.environment['CXXFLAGS'] += ' -I%s/include/freetype2'
#        self.CFLAGS = self.CXXFLAGS = ' -O0 -ggdb3'
