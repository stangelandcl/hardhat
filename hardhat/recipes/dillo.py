from .base import GnuRecipe


class DilloRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DilloRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'db1be16c1c5842ebe07b419aa7c6ef11' \
                      'a45603a75df2877f99635f4f8345148b'
        self.name = 'dillo'
        self.version = '3.0.5'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://www.dillo.org/download/'
        self.depends = ['autotools', 'fltk', 'openssl']
        self.url = 'https://www.dillo.org/download/dillo-$version.tar.bz2'
        self.configure_args += ['--enable-ssl']
