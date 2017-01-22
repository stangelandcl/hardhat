from .base import GnuRecipe
from ..version import extension_regex


class DoxygenRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DoxygenRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'af667887bd7a87dc0dbf9ac8d86c96b5' \
                      '52dfb8ca9c790ed1cbffaa6131573f6b'

        self.name = 'doxygen'
        self.version = '1.8.13'
        self.version_regex = self.name + r'-(?P<version>\d+\.\d+\.\d+)\.src' \
            + extension_regex
        self.version_url = 'http://www.stack.nl/~dimitri/doxygen/download.html'
        self.depends = ['bison', 'cmake', 'flex', 'm4', 'python2']
        self.url = 'http://ftp.stack.nl/pub/doxygen/' \
                   'doxygen-$version.src.tar.gz'

        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]
