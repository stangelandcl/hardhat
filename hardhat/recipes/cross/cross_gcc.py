import os
import shutil
from hardhat.util import check_directory, patch
from hardhat.environment import toolchain_env
from hardhat.urls import Urls
from .gcc_mpfr import CrossGccMpfrRecipe
from .gcc_mpc import CrossGccMpcRecipe
from .gcc_gmp import CrossGccGmpRecipe
from .gcc_isl import CrossGccIslRecipe
from .base import CrossGnuRecipe
from .cross_glibc import CrossGLibCRecipe

HEADERS = set(['linux64.h', 'linux.h', 'sysv4.h'])


class CrossGcc1Recipe(CrossGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossGcc1Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '02f9302a559fa2251595ca0bc1e93721' \
                      '9eff2995a3802d7b31676fec2402beb4'

        self.name = 'cross-gcc1'
        self.version = '6.3.0'
        self.url = Urls.gnu('gcc', 'gcc-%s/gcc-%s.tar.gz'
                            % (self.version, self.version))
        self.extract_dir = os.path.join(self.base_extract_dir,
                                        'cross-gcc-%s' % (self.version))
        self.directory = os.path.join(self.base_extract_dir,
                                      'cross-gcc-%s-build' % (self.version))

        self.prerequisites = [
            CrossGccGmpRecipe(settings=self),
            CrossGccMpcRecipe(settings=self),
            CrossGccMpfrRecipe(settings=self),
            CrossGccIslRecipe(settings=self)
            ]

        for p in self.prerequisites:
            p.gcc_directory = self.extract_dir

        self.environment['SED'] = 'sed'

    def version_check(self):
        pass

    def configure(self):
        super(CrossGcc1Recipe, self).configure()
#        dir = os.path.join(self.extract_dir, 'gcc', 'config')
#        self.log_dir('dynamic linker', dir,
#                     'patching dynamic linker path')
#        headers = set(self._find_headers(dir))
#        for header in headers:
#            self._patch_dynamic_linker(header)

    def clean(self):
        if os.path.exists(self.extract_dir):
            shutil.rmtree(self.extract_dir)
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        for p in self.prerequisites:
            p.reinstall = True
            p.clean()

    def _find_headers_recursive(self, directory, headers):
        for root, dir, files in os.walk(directory):
            for d in dir:
                self._find_headers_recursive(os.path.join(root, d),
                                             headers)
            for file in files:
                if file in HEADERS:
                    headers.append(os.path.join(root, file))

    def _find_headers(self, directory):
        headers = []
        self._find_headers_recursive(directory, headers)
        return headers

    def _patch_header(self, header):
        lib_dir = os.path.join(self.cross_prefix_dir,
                               self.target_triplet,
                               'lib64')

        ld = os.path.join(lib_dir, 'ld')
        usr = os.path.join(self.prefix_dir, 'usr')
        block = '''
        #undef STANDARD_STARTFILE_PREFIX_1
        #undef STANDARD_STARTFILE_PREFIX_2
        #define STANDARD_STARTFILE_PREFIX_1 "%s/"
        #define STANDARD_STARTFILE_PREFIX_2 ""
''' % (lib_dir)

        with open(header, 'rt') as f:
            text = f.read()
        text = text.replace('/lib/ld', ld)
        text = text.replace('/lib64/ld', ld)
        text = text.replace('/lib32/ld', ld)
        text = text.replace('/usr', usr)
        text += block
        with open(header, 'wt') as w:
            w.write(text)

    def _patch_dynamic_linker(self, header):
        linker_dir = os.path.join(self.cross_prefix_dir,
                                  self.target_triplet,
                                  'lib64')
        with open(header, 'rt') as f:
            lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i]
            if line.startswith('#define GLIBC_DYNAMIC_LINKER64'):
                line = '#define GLIBC_DYNAMIC_LINKER64 ' \
                       '"%s/ld-linux-x86-64.so.2"\n' % (linker_dir)
            lines[i] = line
        with open(header, 'wt') as f:
            f.write(''.join(lines))

    def extract(self):
        super(CrossGcc1Recipe, self).extract()

        # See https://wiki.debian.org/Multiarch/LibraryPathOverview
        # For links between configure args and GCC search paths
        check_directory(os.path.join(self.cross_prefix_dir, 'include'))
        check_directory(os.path.join(self.cross_prefix_dir, 'local'))
        glibc = CrossGLibCRecipe(settings=self)
        self.configure_args = self.shell_args + [
            '%s/configure' % self.extract_dir,
            '--target=%s' % (self.target_triplet),
            '--prefix=%s' % (self.cross_prefix_dir),
            '--with-glibc-version=%s' % glibc.version,
            '--with-newlib',
            '--without-headers',
            '--with-local-prefix=%s/%s/local' % (
                self.cross_prefix_dir,
                self.target_triplet),
            '--with-native-system-header-dir=%s/%s/include' % (
                self.cross_prefix_dir,
                self.target_triplet),
            '--enable-languages=c,c++',
            '--disable-multilib',
            '--disable-nls',
            '--disable-shared',
            '--disable-decimal-float',
            '--disable-threads',
            '--disable-libatomic',
            '--disable-libgomp',
            '--disable-libmpx',
            '--disable-libquadmath',
            '--disable-libssp',
            '--disable-libvtv',
            '--disable-libstdcxx',
#            'gcc_cv_libc_provides_ssp=yes'
            ]
        check_directory(self.directory)

    def _download_prequisites(self):
        for prereq in self.prerequisites:
            self.log_dir('prerequisite', self.directory,
                         'running %s' % prereq.name)
            prereq.run()

    def patch(self):
        self.log_dir('patch', self.directory, 'downloading prerequisites')
        self._download_prequisites()
#        cmd = self.shell_args + [
#               'contrib/download_prerequisites'
#               ]
#        self.run_exe(cmd, self.extract_dir, self.environment)

        dir = os.path.join(self.extract_dir, 'gcc', 'config')
        headers = set(self._find_headers(dir))
        for header in headers:
            self._patch_header(header)

        src = r'''if (eval "$ac_cpp conftest.$ac_ext") 2>&5 |
  $EGREP " \",\" " >/dev/null 2>&1; then :
  glibcxx_cv_sys_sdt_h=yes
else
  glibcxx_cv_sys_sdt_h=no
fi'''
        dst = 'glibcxx_cv_sys_sdt_h=no'
        filename = os.path.join(self.extract_dir, 'libstdc++-v3', 'configure')
        patch(filename, src, dst)

        filename = os.path.join(self.extract_dir, 'gcc', 'glimits.h')
        src = '#define MB_LEN_MAX 1'
        dst = '#define MB_LEN_MAX 16'
        patch(filename, src, dst)

#        self._patch_lib64()

    def _patch_lib64(self):
        self.log_dir('patch', self.directory, 'lib to lib64')
        filename = os.path.join(self.extract_dir,
                                'gcc', 'config', 'i386', 't-linux64')
        src = 'm64=../lib64'
        dst = 'm64=../lib'
        patch(filename, src, dst)


    def post_install(self):
        pass  # no ldconfig updating
