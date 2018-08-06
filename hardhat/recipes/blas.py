import os
import shutil
from .base import GnuRecipe


class BlasRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BlasRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '55df2a24966c2928d3d2ab4a20e9856d' \
                      '9914b856cf4742ebd4f7a4507c8e44e8'
        self.name = 'blas'
        self.version = '3.8.0'
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
