import os
from .base import GnuRecipe


class GhcRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GhcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '86a8109dfa4ec000e0048ed9d072c0d2' \
                      '32affeb1069ca96b3995cb5cef2230a7'

        self.name = 'ghc'
        self.version = '8.0.1'
        self.url = 'http://downloads.haskell.org/~$name/$version/' \
                   '$name-$version-x86_64-deb7-linux.tar.xz'
        self.configure_strip_cross_compile()

    def need_configure(self):
        return True

    def extract(self):
        cmd = 'tar xvf %s --directory %s && mv %s/* %s' % (
            self.filename,
            self.directory,
            os.path.join(self.directory, self.name + '-' + self.version),
            self.directory)
        self.log_dir('extract', self.directory, cmd)
        os.makedirs(self.directory)
        os.system(cmd)

    def compile(self):
        pass
