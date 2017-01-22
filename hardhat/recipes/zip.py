from .base import GnuRecipe
from ..urls import Urls


class ZipRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ZipRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f0e8bb1f9b7eb0b01285495a2699df3a' \
                      '4b766784c1765a8f1aeedf63c0806369'

        self.name = 'zip'
        self.version = '3.0'
        self.version_regex = r'(?P<version>\d+\.\d+)/'
        self.version_url = 'https://sourceforge.net/projects/infozip/files/' \
                           'Zip%203.x%20%28latest%29/'
        version = self.version.replace('.', '')
        self.url = 'http://downloads.sourceforge.net/infozip/' \
                   'zip%s.tar.gz' % version

        self.compile_args = ['make',
                             '-f',
                             'unix/Makefile generic_gcc']

        self.install_args = ['make',
                             'prefix=%s' % self.prefix_dir,
                             '-f',
                             'unix/Makefile',
                             'install']

    def configure(self):
        pass
