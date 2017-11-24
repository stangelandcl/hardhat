import os
from .base import GnuRecipe
from ..util import patch


class CLuceneRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CLuceneRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'cb6babf970dd31159a622fe4cd935e2e' \
                      'd78a968be8412f9838ab9e0184d6b298'
        self.name = 'clucene'
        self.version = 'e8e3d20f20da5ee3e37d347207b01890829a5475'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools']
        self.url = 'https://sourceforge.net/code-snapshots/git/c/cl/clucene/' \
                   'code.git/clucene-code-$version.zip'
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]

    def extract(self):
        self.log_dir('extract', self.directory, 'extracting')
        self.extract_args = ['unzip', self.filename, '-d', self.directory]
        self.run_exe(self.extract_args, self.tarball_dir, self.environment)
        self.directory = os.path.join(
            self.directory, 'clucene-code-' + self.version)

    def patch(self):
        src = 'MACRO_CHECK_GCC_VISIBILITY(_CL_HAVE_GCCVISIBILITYPATCH)'
        file = os.path.join(self.directory, 'src/core/CMakeLists.txt')
        patch(file, src, '')

        file = os.path.join(self.directory, 'src/shared/CMakeLists.txt')
        patch(file, src, '')
