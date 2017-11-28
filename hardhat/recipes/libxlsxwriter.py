from .base import GnuRecipe


class LibXlsxWriterRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXlsxWriterRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9b57d9cc989e552e4ac6366b7bac0950' \
                      'aeab0bc7032a8c18a5d5b33132f0de9c'

        self.name = 'libxlsxwriter'
        self.version = '0.7.5'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'pkgconfig', 'zlib']
        self.url = 'https://github.com/jmcnamara/libxlsxwriter/archive/' \
                   'RELEASE_$version.tar.gz'
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]
