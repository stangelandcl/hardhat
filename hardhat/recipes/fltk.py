from .base import GnuRecipe
from ..version import Versions


class FltkRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FltkRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c8ab01c4e860d53e11d40dc28f98d2fe' \
                      '9c85aaf6dbb5af50fd6e66afec3dc58f'

        self.name = 'fltk'
        self.depends = ['hicolor-icon-theme', 'libjpeg-turbo', 'libpng',
                        'xorg-libs']

        self.version = '1.3.4'
        self.version_regex = r'(?P<version>1\.3\.\d+)/'
        self.version_url = 'http://fltk.org/pub/fltk/'
        self.url = 'http://fltk.org/pub/fltk/$version/' \
                   'fltk-$version-source.tar.gz'

    def need_configure(self):
        return True
