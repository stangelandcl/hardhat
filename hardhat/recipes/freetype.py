import os
from .base import GnuRecipe


class FreetypeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FreetypeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'db8d87ea720ea9d5edc5388fc7a0497b' \
                      'b11ba9fe972245e0f7f4c7e8b1e1e84d'

        self.name = 'freetype'
        self.version = '2.9.1'
        self.version_url = 'http://download.savannah.gnu.org/releases/' \
                           'freetype/'
        self.url = 'http://downloads.sourceforge.net/freetype/' \
                   'freetype-$version.tar.bz2'

    def need_configure(self):
        return True

    def patch(self):
        self.log_dir('patch', self.directory, 'modules.cfg')
        file = os.path.join(self.directory, 'modules.cfg')
        with open(file, 'rt') as f:
            text = f.read()
        text = text.replace('# AUX_MODULES += gxvalid',
                            'AUX_MODULES += gxvalid')
        text = text.replace('# AUX_MODULES += otvalid',
                            'AUX_MODULES += otvalid')
        with open(file, 'wt') as f:
            f.write(text)

        self.log_dir('patch', self.directory, 'ftoption.h')
        file = os.path.join(self.directory,
                            'include/freetype/config/ftoption.h')
        with open(file, 'rt') as f:
            text = f.read()
        text = text.replace(
            '/* #define FT_CONFIG_OPTION_SUBPIXEL_RENDERING */',
            '#define FT_CONFIG_OPTION_SUBPIXEL_RENDERING')
        text = text.replace(
            '/* #define TT_CONFIG_OPTION_SUBPIXEL_HINTING */',
            '#define TT_CONFIG_OPTION_SUBPIXEL_HINTING')
        with open(file, 'wt') as f:
            f.write(text)
