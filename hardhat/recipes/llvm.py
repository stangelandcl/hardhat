import os
import shutil
from string import Template
from .base import Downloader, GnuRecipe
from hardhat.tarball import Tarball
from hardhat.version import extension_regex
from hardhat.util import patch


class Extra:
    def __init__(self, name):
        self.sha256 = None
        self.name = name


class LlvmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LlvmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8d10511df96e73b8ff9e7abbfb4d4d43' \
                      '2edbdbe965f1f4f07afaf370b8a533be'
        self.name = 'llvm'
        self.version = '4.0.0'
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
                                       'llvm-clang-%s.tar.xz' % self.version)
        self.clang_dir = os.path.join(self.base_extract_dir,
                                      'clang-%s' % self.version)
        self.compiler_rt_url = Template('http://llvm.org/releases/$version/'
                                        'compiler-rt-$version.src.tar.xz') \
                                        .substitute(version=self.version)
        self.compiler_rt_file = os.path.join(
            self.tarball_dir,
            'llvm-compiler-rt-%s.tar.xz' % self.version)
        self.compiler_rt_dir = os.path.join(self.base_extract_dir,
                                            'compiler-rt-%s' % self.version)

        self.openmp_url = Template('http://llvm.org/releases/$version/' \
                                   'openmp-$version.src.tar.xz') \
                                   .substitute(version=self.version)
        self.openmp_file = os.path.join(self.tarball_dir,
                                        'llvm-openmp-%s.tar.xz' % self.version)
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
                             '-DLLVM_ENABLE_FFI=ON',
                             '-DCMAKE_BUILD_TYPE=Release',
#                             '-DBUILD_SHARED_LIBS=ON',
                             '-DLLVM_BUILD_LLVM_DYLIB=ON',
                             '-DLLVM_TARGETS_TO_BUILD="host;AMDGPU"',
                             '-DGCC_INSTALL_PREFIX=%s' % self.prefix_dir,
                             '-DLLVM_DEFAULT_TARGET_TRIPLE=%s'
                             % self.target_triplet,
                             '-DLLVM_TARGET_ARCH=x86_64',
#                             '-DLLVM_TARGETS_TO_BUILD=x86_64',
#                             '-DCMAKE_CXX_LINK_FLAGS="%s"' % self.prefix_dir,
                             '-Wno-dev',
                             '..']

        self.clang = Extra('llvm-clang')
        self.clang.url = self.clang_url
        self.clang.filename = self.clang_file
        self.clang.version = self.version
        self.clang.sha256 = 'cea5f88ebddb30e296ca89130c83b9d4' \
                            '6c2d833685e2912303c828054c4dc98a'

        self.compiler_rt = Extra('llvm-compiler_rt')
        self.compiler_rt.url = self.compiler_rt_url
        self.compiler_rt.filename = self.compiler_rt_file
        self.compiler_rt.version = self.version
        self.compiler_rt.sha256 = 'd3f25b23bef24c305137e6b44f7e81c5' \
                                  '1bbec764c119e01512a9bd2330be3115'

        self.openmp = Extra('llvm-openmp')
        self.openmp.url = self.openmp_url
        self.openmp.filename = self.openmp_file
        self.openmp.version = self.version
        self.openmp.sha256 = 'db55d85a7bb289804dc42fc5c8e35ca2' \
                             '4dfc3885782261b675a194fd7e206e26'


        self.extra_downloads = [
            self.clang,
            self.compiler_rt,
            self.openmp
            ]

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
        self.old_dir = self.directory
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
        text = """#!/bin/bash
install -v -m644 docs/man/* $prefix/share/man/man1             &&
install -v -d -m755 $prefix/share/doc/llvm-$version/llvm-html     &&
cp -Rv docs/html/* $prefix/share/doc/llvm-$version/llvm-html
The cmake documentation can be installed in the same way (again as the root user):

install -v -m644 tools/clang/docs/man/* $prefix/share/man/man1 &&
install -v -d -m755 $prefix/share/doc/llvm-$version/clang-html    &&
cp -Rv tools/clang/docs/html/* $prefix/share/doc/llvm-$version/clang-html
""".replace('$prefix', self.prefix_dir).replace('$version', self.version)

        self.directory = self.old_dir
        self.log_dir('install', self.directory, 'install docs')
        script = os.path.join(self.directory, 'install_docs.sh')
        with open(script, 'wt') as f:
            f.write(text)

        args = self.shell_args + [script]
        self.run_exe(args, self.directory, self.environment)
