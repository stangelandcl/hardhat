from .base import GnuRecipe


class ExempiRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ExempiRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0e7ad0e5e61b6828e38d31a8cc59c26c' \
                      '9adeed7edf4b26708c400beb6a686c07'

        self.name = 'exempi'
        self.depends = ['boost']
        self.version = '2.2.2'
        self.url = 'http://libopenraw.freedesktop.org/download/' \
                   'exempi-$version.tar.bz2'
        self.configure_args += ['--with-boost=%s' % self.prefix_dir]
