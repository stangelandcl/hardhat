import os
import shutil
from string import Template
from .base import Downloader, GnuRecipe
from hardhat.tarball import Tarball
from hardhat.version import extension_regex
from hardhat.util import patch


class LlvmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LlvmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1fd90354b9cf19232e8f168faf2220e7' \
                      '9be555df3aa743242700879e8fd329ee'

        self.name = 'llvm'
        self.version = '3.9.1'
        self.version_regex = self.name + '\-(?P<version>\d+\.\d+\.\d+).*' \
            + extension_regex
        self.version_url = 'http://releases.llvm.org/download.html'
        self.depends = ['cmake', 'doxygen', 'libffi',
                        'libxml2', 'python2', 'python3-sphinx',
                        'valgrind', 'zip']
        self.url = 'http://llvm.org/releases/$version/llvm-$version.src.tar.xz'
        self.clang_url = Template('http://llvm.org/releases/$version/'
                                  'cfe-$version.src.tar.xz').substitute(
                                      version=self.version)
        self.clang_file = os.path.join(self.tarball_dir,
                                       'clang-%s.tar.xz' % self.version)
        self.clang_dir = os.path.join(self.base_extract_dir,
                                      'clang-%s' % self.version)
        self.compiler_rt_url = Template('http://llvm.org/releases/$version/'
                                        'compiler-rt-$version.src.tar.xz') \
                                        .substitute(version=self.version)
        self.compiler_rt_file = os.path.join(
            self.tarball_dir,
            'compiler-rt-%s.tar.xz' % self.version)
        self.compiler_rt_dir = os.path.join(self.base_extract_dir,
                                            'compiler-rt-%s' % self.version)

        self.openmp_url = Template('http://llvm.org/releases/$version/' \
                                   'openmp-$version.src.tar.xz') \
                                   .substitute(version=self.version)
        self.openmp_file = os.path.join(self.tarball_dir,
                                        'openmp-%s.tar.xz' % self.version)
        self.openmp_dir = os.path.join(self.base_extract_dir,
                                       'openmp-%s' % self.version)

        lib_dirs = ['%s\lib',
                    '%s\lib64',
                    '%s\%s\lib',
                    '%s\%s\lib64']
        link_flags = ''
        for lib in lib_dirs:
            link_flags += '-L%s ' % lib

        for lib in lib_dirs:
            link_flags += '-Wl,-rpath,%s ' % lib

        self.compile_args = ['cmake',
                             '-G',
                             '"Unix Makefiles"',
                             '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
                             '-DLLVM_ENABLE_FFI=on',
                             '-DCMAKE_BUILD_TYPE=Release',
                             '-DBUILD_SHARED_LIBS=ON',
                             '-DLLVM_TARGETS_TO_BUILD="host;AMDGPU"',
                             '-DGCC_INSTALL_PREFIX=%s' % self.prefix_dir,
                             '-DLLVM_DEFAULT_TARGET_TRIPLE=%s'
                             % self.target_triplet,
                             '-DLLVM_TARGET_ARCH=x86_64',
#                             '-DLLVM_TARGETS_TO_BUILD=x86_64',
#                             '-DCMAKE_CXX_LINK_FLAGS="%s"' % self.prefix_dir,
                             '-Wno-dev',
                             '..']

    def need_configure(self):
        return False

    def clean(self):
        super(LlvmRecipe, self).clean()

        if os.path.exists(self.clang_dir):
            self.log_dir('clean', self.clang_dir, 'removing')
            shutil.rmtree(self.clang_dir)

        if os.path.exists(self.compiler_rt_dir):
            self.log_dir('clean', self.compiler_rt_dir, 'removing')
            shutil.rmtree(self.compiler_rt_dir)

        if os.path.exists(self.openmp_dir):
            self.log_dir('clean', self.openmp_dir, 'removing')
            shutil.rmtree(self.openmp_dir)

    def download(self):
        super(LlvmRecipe, self).download()

        d = Downloader()
        d.name = ''
        d.version = ''
        d.quiet = self.quiet
        d.silent = self.silent
        d.log = self.log
        d.log_dir = self.log_dir
        d.sha256 = 'e6c4cebb96dee827fa0470af313dff26' \
                   '5af391cb6da8d429842ef208c8f25e63'
        d.url = self.clang_url
        d.filename = self.clang_file
        d.download()

#        save_url(self.clang_url, self.clang_file)
        d = Downloader()
        d.name = ''
        d.version = ''
        d.quiet = self.quiet
        d.silent = self.silent
        d.log = self.log
        d.log_dir = self.log_dir
        d.sha256 = 'd30967b1a5fa51a2503474aacc913e69' \
                   'fd05ae862d37bf310088955bdb13ec99'
        d.url = self.compiler_rt_url
        d.filename = self.compiler_rt_file
        d.download()
 #       save_url(self.compiler_rt_url, self.compiler_rt_file)

        d = Downloader()
        d.name = ''
        d.version = ''
        d.quiet = self.quiet
        d.silent = self.silent
        d.log = self.log
        d.log_dir = self.log_dir
        d.sha256 = 'd23b324e422c0d5f3d64bae5f550ff11' \
                   '32c37a070e43c7ca93991676c86c7766'
        d.url = self.openmp_url
        d.filename = self.openmp_file
        d.download()

    def patch(self):
        # don't overwrite gcc's libgomp. It doesn't work with
        # clang's version
        src = r'set(LIBOMP_ALIASES "libgomp;libiomp5")'
        dst = r'set(LIBOMP_ALIASES "")'
        filename = os.path.join(self.openmp_dir, 'runtime', 'src',
                                'CMakeLists.txt')
        patch(filename, src, dst)


    def extract(self):
        super(LlvmRecipe, self).extract()

        if not os.path.exists(self.clang_dir):
            self.log_dir('extract', self.clang_dir, self.clang_file)
            with Tarball(self.clang_file) as f:
                f.extract(self.clang_dir)
            os.symlink(self.clang_dir,
                       os.path.join(self.directory, 'tools', 'clang'))

        if not os.path.exists(self.compiler_rt_dir):
            self.log_dir('extract', self.compiler_rt_dir,
                         self.compiler_rt_file)
            with Tarball(self.compiler_rt_file) as f:
                f.extract(self.compiler_rt_dir)
            os.symlink(self.compiler_rt_dir,
                       os.path.join(self.directory, 'projects', 'compiler-rt'))

        if not os.path.exists(self.openmp_dir):
            self.log_dir('extract', self.openmp_dir,
                         self.openmp_file)
            with Tarball(self.openmp_file) as f:
                f.extract(self.openmp_dir)
            os.symlink(self.openmp_dir,
                       os.path.join(self.directory, 'projects', 'openmp'))

    def compile(self):
        self.directory = os.path.join(self.directory, 'build')
        os.makedirs(self.directory)
        super(LlvmRecipe, self).compile()

        self.compile_args = ['make',
                             '-j%s' % self.cpu_count]
        super(LlvmRecipe, self).compile()

        self.compile_args = ['cmake',
                             '-DLLVM_ENABLE_SPHINX=ON',
                             '-DSPHINX_WARNINGS_AS_ERRORS=OFF',
#                             '-DLLVM_ENABLE_DOXYGEN=ON',
                             '-Wno-dev',
                             '..']
        super(LlvmRecipe, self).compile()

        self.compile_args = ['make',
                             'docs-clang-html',
                             'docs-clang-man',
                             'docs-llvm-html',
                             'docs-llvm-man',
#                             'doxygen-clang',
#                             'doxygen-llvm'
                             ]
        super(LlvmRecipe, self).compile()

    def install(self):
        super(LlvmRecipe, self).install()
        """ TODO: from LFS
install -v -m644 docs/man/* /usr/share/man/man1             &&
install -v -d -m755 /usr/share/doc/llvm-3.8.0/llvm-html     &&
cp -Rv docs/html/* /usr/share/doc/llvm-3.8.0/llvm-html
The cmake documentation can be installed in the same way (again as the root user):

install -v -m644 tools/clang/docs/man/* /usr/share/man/man1 &&
install -v -d -m755 /usr/share/doc/llvm-3.8.0/clang-html    &&
cp -Rv tools/clang/docs/html/* /usr/share/doc/llvm-3.8.0/clang-html
"""
