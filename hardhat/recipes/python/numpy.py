import os
from string import Template
from .base import SetupPyRecipe


class NumpyRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(NumpyRecipe, self).__init__(*args, **kwargs)
        self.depends = ['openblas', 'python3-cython']
        self.name = 'numpy'
        self.version = '1.11.0'
        self.sha256 = 'e898e1f2b89092b95352a0a583152a18' \
                      '4020a492ae77a38be03379d90f575996'
        self.url = 'https://github.com/numpy/numpy/archive/v$version.tar.gz'
        self.filename = os.path.join(self.tarball_dir,
                                     'numpy-%s.tar.gz' % (self.version))

        self.environment['LDFLAGS'] += ' -shared'

    def patch(self):
        text = Template("""
[DEFAULT]
libraries = openblas
library_dirs = $lib_dir
include_dirs = $include_dir
runtime_library_dirs = $lib_dir
search_static_first = false

[atlas]
atlas_libs = openblas
libraries = openblas
library_dirs = $lib_dir
include_dirs = $include_dir
runtime_library_dirs = $lib_dir

[openblas]
openblas_libs = openblas
libraries = openblas
library_dirs = $lib_dir
include_dirs = $include_dir
runtime_library_dirs = $lib_dir

[lapack]
lapack_libs = openblas
libraries = openblas
library_dirs = $lib_dir
include_dirs = $include_dir
runtime_library_dirs = $lib_dir

""").substitute(lib_dir=os.path.join(self.prefix_dir, 'lib'),
                include_dir=os.path.join(self.prefix_dir, 'include'))
        # openblas must be compiled with pthreads. See site.cfg.examlpe for why

        file = os.path.join(self.directory, 'site.cfg')
        with open(file, 'wt') as f:
            f.write(text)
