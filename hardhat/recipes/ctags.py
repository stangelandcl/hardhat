from .base import GnuRecipe
from ..urls import Urls


class CtagsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CtagsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e1f5909ec0c7a58fd2149139fa6a1dc5' \
                      '32070a3d919dd183671c57a32f8b243d'

        self.name = 'ctags'
        self.version = '5.8'
        v = self.version.replace('.', '')
        self.url = 'https://downloads.sourceforge.net/ctags/' \
                   'ctags/%s/ctags%s.zip' % (self.version, v)

    def extract(self):
        self.log_dir('extract', self.directory, 'extracting')

        self.extract_args = ['unzip', self.filename, '-d', self.directory]
        self.run_exe(self.extract_args, self.tarball_dir, self.environment)
