from .base import GnuRecipe


class FdkAacRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FdkAacRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5910fe788677ca13532e3f47b7afaa01' \
                      'd72334d46a2d5e1d1f080f1173ff15ab'

        self.name = 'fdk-aac'
        self.version = '0.1.4'
        self.url = 'http://downloads.sourceforge.net/opencore-amr/' \
                   'fdk-aac-$version.tar.gz'
        self.environment['CXXFLAGS'] += ' -Wno-narrowing'
