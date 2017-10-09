import os
from .base import GnuRecipe


class Extra:
    def __init__(self, name):
        self.name = name
        self.sha256 = None


class Mingw64Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Mingw64Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '5f46e80ff1a9102a37a3453743dae9df' \
                      '98262cba7c45306549ef7432cfd92cfd'

        self.name = 'mingw64'
        self.version = '5.0.2'
        self.url = 'http://downloads.sourceforge.net/project/mingw-w64/' \
                   'mingw-w64/mingw-w64-release/mingw-w64-v$version.tar.bz2'

        self.configure_strip_cross_compile()
        self.configure_args += ['--build=%s' % self.target_triplet,
                                '--host=%s' % self.target_triplet,
                                '--with-tools=all']

        self.mingw64_dir = os.path.join(self.prefix_dir, 'mingw64')
        self.target64 = 'x86_64-w64-mingw32'
        self.target32 = 'i686-w64-mingw32'

        # See docs in mingw64-w64-doc/howto-build
        # This requires a multi stage building including binutils, and gcc in
        # multiple steps

        self.binutils = Extra('binutils')
        self.binutils.url = 'http://ftp.gnu.org/gnu/binutils/' \
                            'binutils-$version.tar.bz2'
        self.binutils.version = '2.28'
        self.binutils.sha256 = '6297433ee120b11b4b0a1c8f3512d7d7' \
                               '3501753142ab9e2daa13c5a3edd32a72'
        self.binutils_configure_args = self.shell_args + [
            '../configure',
            '--prefix=%s' % self.mingw64_dir,
            '--with-sysroot=%s' % self.mingw64_dir,
            '--enable-targets=%s,%s' % (self.target32, self.target64),
            ]

        self.gcc = Extra('gcc')
        self.gcc.url = 'http://ftpmirror.gnu.org/gcc/gcc-$version/' \
                       'gcc-$version.tar.bz2'
        self.gcc.version = '7.1.0'
        self.gcc.sha256 = '8a8136c235f64c6fef69cac0d73a46a1' \
                          'a09bb250776a050aec8f9fc880bebc17'
        self.extra_downloads += [self.binutils, self.gcc]
        self.headers_build_dir = os.path.join(self.directory, 'build-headers')
        self.headers_configure_args = self.shell_args + [
            '../mingw-w64-headers/configure',
            '--prefix=%s' % self.mingw64_dir,
            '--host=%s' % self.target64,
            '--build=%s' % self.build_triplet
            ]

    def download(self):
        super(Mingw64Recipe, self).download()
        self.binutils_dir = os.path.join(
            self.directory,
            os.path.basename(self.binutils.filename).replace('.tar.bz2', ''))
        self.binutils_build_dir = os.path.join(self.binutils_dir, 'build')

        self.gcc_dir = os.path.join(
            self.directory,
            os.path.basename(self.gcc.filename).replace('.tar.bz2', ''))
        self.gcc_build_dir = os.path.join(self.gcc_dir, 'build')

    def extract(self):
        super(Mingw64Recipe, self).extract()

        self.log_dir('extract', self.directory, 'binutils')
        self.extract_into(self.binutils.filename, self.directory)
        os.makedirs(self.binutils_build_dir)

        self.log_dir('extract', self.directory, 'gcc')
        self.extract_into(self.gcc.filename, self.directory)
        os.makedirs(self.gcc_build_dir)

        os.makedirs(self.headers_build_dir)

    def configure(self):
        self.log_dir('configure',
                     self.binutils_build_dir,
                     'configure binutils')
        self.run_exe(self.binutils_configure_args,
                     self.binutils_build_dir,
                     self.environment)

        self.log_dir('configure', self.binutils_build_dir, 'make binutils')
        self.run_exe(['make', '-j%s' % self.cpu_count],
                     self.binutils_build_dir,
                     self.environment)

        self.log_dir('configure', self.binutils_build_dir, 'install binutils')
        self.run_exe(['make', 'install'],
                     self.binutils_build_dir,
                     self.environment)

        self.log_dir('configure', self.headers_build_dir, 'configure headers')
        self.run_exe(self.headers_configure_args,
                     self.headers_build_dir,
                     self.environment)

        self.log_dir('configure', self.headers_build_dir, 'install headers')
        self.run_exe(['make', 'install'],
                     self.headers_build_dir,
                     self.environment)

    def compile(self):
        pass

    def install(self):
        pass
