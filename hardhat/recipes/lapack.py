import os
import shutil
from .base import GnuRecipe


class LapackRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LapackRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a9a0082c918fe14e377bbd5700576167' \
                      '68dca76cbdc713457d8199aaa233ffc3'
        self.name = 'lapack'
        self.version = '3.6.0'
        self.url = 'http://www.netlib.org/lapack/lapack-$version.tgz'

        self.libname = 'liblapack.a'

        self.compile_args = ['make',
                             'lapacklib',
                             'OPTS="-O3 -fomit-frame-pointer -funroll-loops'
                             ' -flto -ffat-lto-objects"',
                             'LOADOPTS="-fPIC -flto -fuse-linker-plugin"'
                             ]


    def patch(self):
        src = os.path.join(self.directory, 'make.inc.example')
        dest = os.path.join(self.directory, 'make.inc')
        shutil.copy2(src, dest)

    def compile(self):
        super(LapackRecipe, self).compile()

#        self.compile_args = ['make']
#        self.log_dir('compile', self.directory, ' '.join(self.compile_args))
#        self.run_exe(self.compile_args, self.directory, self.environment)

    def install(self):
        src = os.path.join(self.directory, self.libname)
        dest = os.path.join(self.prefix_dir, 'lib', self.libname)
        shutil.copy2(src, dest)
