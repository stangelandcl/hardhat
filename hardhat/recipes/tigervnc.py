from .base import GnuRecipe
from ..urls import Urls


class TigerVncRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TigerVncRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4aa704747b4f8f1d59768b663c488fa9' \
                      '37e6783db2a46ae407cd2a599cfbf8b1'

        self.name = 'tigervnc'
        self.depends = ['cmake', 'fltk', 'libjpeg-turbo', 'libpng']
        self.version = '1.7.0'
        self.url = Urls.github_commit(
            'TigerVNC', self.name, 'v' + self.version)
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '-Wno-dev'
            ]
#        self.environment['LIBS'] += ' -lpng -ldl -fPIC'
        self.environment['CXXFLAGS'] += ' -fPIC'
        self.environment['LDFLAGS'] += ' -lpng -ldl'
