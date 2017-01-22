import os
from hardhat.util import patch
from .base import GnuRecipe


class GeosRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GeosRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4a2e4e3a7a09a7cfda3211d0f4a235d9' \
                      'fd3176ddf64bd8db14b4ead266189fc5'

        self.name = 'geos'
        self.version = '3.6.1'
        self.url = 'http://download.osgeo.org/geos/geos-$version.tar.bz2'
        self.environment['CXXFLAGS'] += ' -Wno-deprecated-declarations'
        self.environment['CFLAGS'] += ' -Wno-deprecated-declarations'
        self.environment_strip_lto()

    def patch(self):
        filename = os.path.join(self.directory, 'include/geos/platform.h.in')
        src = '#ifndef ISNAN'
        dst = '#define ISNAN(n) std::isnan(n)\n' \
              '#ifndef ISNAN'

        patch(filename, src, dst)
