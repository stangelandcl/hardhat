import os
from .base import GnuRecipe


class FreeFontRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FreeFontRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7c85baf1bf82a1a1845d1322112bc6ca' \
                      '982221b484e3b3925022e25b5cae89af'

        self.depends = ['fontconfig', 'unzip']
        self.name = 'freefont'
        self.version = '20120503'
        self.url = 'ftp://ftp.gnu.org/pub/gnu/freefont/' \
                   'freefont-ttf-$version.zip'
        self.install_args = [['install', '-v', '-d', '-m755',
                              '%s/share/fonts/freefont' % self.prefix_dir],
                             ['install', '-v', '-m644', '*.ttf',
                              '%s/share/fonts/freefont' % self.prefix_dir]]

    def extract(self):
        self.log_dir('extract', self.directory, 'extracting')

        self.extract_args = ['unzip', self.filename, '-d', self.directory]
        self.run_exe(self.extract_args, self.tarball_dir, self.environment)
        self.directory = os.path.join(self.directory,
                                      'freefont-%s' % self.version)

    def configure(self):
        pass

    def compile(self):
        pass

    def post_install(self):
        self.log_dir('post-install', self.directory, 'fc-cache')
        self.run_exe(['fc-cache'], self.directory, self.environment)
