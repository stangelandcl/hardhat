import os
import shutil
from sys import platform
from .base import GnuRecipe
from ..urls import Urls


class OpenBlasRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpenBlasRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9c40b5e4970f27c5f6911cb0a28aa26b' \
                      '6c83f17418b69f8e5a116bb983ca8557'

        self.name = 'openblas'
        self.version = '0.2.19'
        self.url = Urls.github_commit('xianyi', 'OpenBLAS',
                                      'v' + self.version)
#        self.filename = os.path.join(self.tarball_dir,
#                                     'openblas-%s.tar.gz' % self.version)
        self.libname = 'libopenblas.a'

        del self.environment['CPPFLAGS']
        del self.environment['CXXFLAGS']
        self.environment['CFLAGS'] = '-fomit-frame-pointer' \
                                     ' -funroll-loops'
        self.environment['FFLAGS'] = '-fomit-frame-pointer' \
                                     ' -funroll-loops'

        self.compile_args += ['USE_THREAD=1',
                              'FC=gfortran',
                              'BINARY=64',
                              ]
# If needed. See TargetList.txt in OpenBLAS directory for list of targets
        if self.is_atom():
            self.compile_args += ['TARGET=ATOM']

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
