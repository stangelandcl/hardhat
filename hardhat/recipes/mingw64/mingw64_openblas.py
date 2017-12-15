import os
import shutil
from sys import platform
from .base import Mingw64BaseRecipe
from hardhat.urls import Urls
from hardhat.util import patch


class Mingw64OpenBlasRecipe(Mingw64BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Mingw64OpenBlasRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c4f71a60e3f23a7a25693390af3be230' \
                      '8d374749ae3cb0bcfd8aab33a3c9ac09'

        self.name = 'mingw64-openblas'
        self.version = 'fd4e68128e56beb3b97f37178edf07bef7ade5f1'
        self.url = Urls.github_commit('xianyi', 'OpenBLAS',
                                      self.version)
#        self.filename = os.path.join(self.tarball_dir,
#                                     'openblas-%s.tar.gz' % self.version)
        self.libname = 'libopenblas.a'

        del self.environment['CPPFLAGS']
        del self.environment['CXXFLAGS']
        self.environment['CFLAGS'] = '-fomit-frame-pointer' \
                                     ' -funroll-loops'
        self.environment['FFLAGS'] = '-fomit-frame-pointer' \
                                     ' -funroll-loops'

        os.environ['GFORTRAN'] = 'x86_64-w64-mingw32-gfortran'
        self.compile_args += ['USE_THREAD=1',
                              'FC=gfortran',
#                              'CC=%s' % os.environ['CC'],
                              'FC=%s' % os.environ['GFORTRAN'],
                              'BINARY=64',
#                              'HOSTCC=%s' % os.environ['CC'],
#                              'AS=%s' % os.environ['AS'],
#                              'CROSS=1',
 #                             'LD=%s' % os.environ['LD'],
#                              'CROSS_SUFFIX=x86_64-w64-mingw32-'
                              ]
# If needed. See TargetList.txt in OpenBLAS directory for list of targets
        if self.is_atom():
            self.compile_args += ['TARGET=ATOM']
        else:
            # hardcoded because it failed to compile when detecting for itself
            self.compile_args += ['TARGET=CORE2']

#        self.compile_args = ['make',
#                             'all',
#                             'BLASLIB=%s' % (self.libname),
#                             'OPTS="-O3 -fomit-frame-pointer -funroll-loops"'
#                             ]  # not parallel safe

        self.install_args += ['PREFIX=%s' % (self.prefix_dir)
                              ]

    def is_atom(self):
        lines = []
        if platform == "linux" or platform == "linux2":
            with open('/proc/cpuinfo', 'rt') as f:
                lines = f.readlines()

        for line in lines:
            if line.startswith('model name'):
                model = line[len('model_name'):].strip()
                model = model[2:]
                if 'Intel(R) Celeron(R) CPU  N2940' in model:
                    return True
                break
        return False

    def patch(self):
        self.log_dir('patch', self.directory, 'patching getarch')
        filename = os.path.join(self.directory, 'Makefile.prebuild')
        src = './getarch_2nd'
        dst = '%s/../bin/wine64 ./getarch_2nd' % self.prefix_dir
        patch(filename, src, dst)

        src = './getarch '
        dst = '%s/../bin/wine64 ./getarch ' % self.prefix_dir
        patch(filename, src, dst)


    def configure(self):
        pass

#    def install(self):
#        super(OpenBlasRecipe, self).install()
#
#        libs = ['libopenblas.a',
#                'libopenblas.so.0',
#                'libopenblas.so']
#
#        for lib in libs:
#            src = os.path.join(self.directory, 'lib', lib)
#            dest = os.path.join(self.prefix_dir, 'lib', lib)
#            shutil.copy2(src, dest)
