import os
import shutil
from .base import GnuRecipe


class BlasRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BlasRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'bd62d5791b90702ddc99b64136951c6d' \
                      '665dd7dfdb641c0d5fd30a56559a66b8'
        self.name = 'blas'
        self.version = '3.6.0'
        self.url = 'http://www.netlib.org/blas/blas-$version.tgz'
        self.libname = 'libblas.a'

        self.compile_args = ['make',
                             'all',
                             'BLASLIB=%s' % (self.libname),
                             'OPTS="-O3 -fomit-frame-pointer -funroll-loops'
                             ' -flto -ffat-lto-objects"',
                             'LOADOPTS="-fPIC -flto -fuse-linker-plugin"'
                             ]  # not parallel safe

    def install(self):
        src = os.path.join(self.directory, self.libname)
        dest = os.path.join(self.prefix_dir, 'lib', self.libname)
        shutil.copy2(src, dest)
