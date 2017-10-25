import os
import shutil
from .base import GnuRecipe


class EigenRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(EigenRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'dd254beb0bafc695d0f62ae1a222ff85' \
                      'b52dbaa3a16f76e781dce22d0d20a4a6'

        self.name = 'eigen'
        self.version = '3.3.4'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'pcre', 'pkgconfig', 'xz', 'zlib']
        self.url = 'http://bitbucket.org/eigen/eigen/get/$version.tar.bz2'
#        self.configure_args = ['cmake',
#                               '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
#                               '..']

    def extract(self):
        super(EigenRecipe, self).extract()

#        src = os.path.join(self.directory, 'build')
#        os.makedirs(src)
#        self.directory = src

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        src = os.path.join(self.directory, 'Eigen')
        dst = os.path.join(self.prefix_dir, 'include', 'Eigen')

        if os.path.exists(dst):
            shutil.rmtree(dst)

        shutil.copytree(src, dst)
