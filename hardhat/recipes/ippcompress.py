from .base import GnuRecipe


class IppCompressRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(IppCompressRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3d0d4da69e65c46fc97c3713aa4f56ca' \
                      'b23f3edca76bded26e4db857dc9efd1f'

        self.depends = ['unzip']
        self.name = 'ippcompress'
        self.description = 'Intel GZip'
        self.version = '0.1'
        self.url = 'http://btweb.phibred.com/devel/files/' \
                   'IppCompress-linux-x64-$version.zip'
        self.install_args = ['make',
                             'install',
                             'DESTDIR=%s' % self.prefix_dir]

    def extract(self):
        self.log_dir('extract', self.directory, 'extracting')

        self.extract_args = ['unzip', self.filename, '-d', self.directory]
        self.run_exe(self.extract_args, self.tarball_dir, self.environment)

    def configure(self):
        pass

    def compile(self):
        pass
