import os
import shutil
from hardhat.util import check_directory, patch
from hardhat.environment import target_path_env
from hardhat.urls import Urls
from .gcc_mpfr import GccMpfrRecipe
from .gcc_mpc import GccMpcRecipe
from .gcc_gmp import GccGmpRecipe
from .gcc_isl import GccIslRecipe
from hardhat.recipes.cross.base import CrossGnuRecipe
from string import Template
import hardhat
import stat
from ..base import GnuRecipe


HEADERS = set(['linux64.h', 'linux.h', 'sysv4.h'])


class GccPrereqRecipesMixin:
    def __init__(self, *args, **kwargs):
        super(GccPrereqRecipesMixin, self).__init__()
        prefix = kwargs.get('prefix', '')
        gcc_directory = kwargs.get('gcc_directory', self.extract_dir)
        self.gmp = GccGmpRecipe(settings=self)
        self.mpc = GccMpcRecipe(settings=self)
        self.mpfr = GccMpfrRecipe(settings=self)
        self.isl = GccIslRecipe(settings=self)
        self.prerequisites = [
            self.gmp, self.mpc, self.mpfr, self.isl
            ]

        for p in self.prerequisites:
            p.name = prefix + p.name
            p.gcc_directory = gcc_directory
            p.environment = self.environment
            p.reinstall = True

    def clean(self):
        for p in self.prerequisites:
            p.reinstall = True
            p.clean()

    def patch(self):
        self.log_dir('patch', self.directory, 'downloading prerequisites')
        self._download_prequisites()

    def _download_prequisites(self):
        for prereq in self.prerequisites:
            self.log_dir('prerequisite', self.directory,
                         'running %s' % prereq.name)
            prereq.run()


class GccRecipe(CrossGnuRecipe, GccPrereqRecipesMixin):
    def __init__(self, *args, **kwargs):
        super(GccRecipe, self).__init__(*args, **kwargs)
        self.sha256 = self.gcc_sha256
        self.name = 'gcc'
        self.version = self.gcc_version
        self.post_clean = False
        self.url = Urls.gnu('gcc', 'gcc-%s/gcc-%s.tar.gz'
                            % (self.version, self.version))
        self.environment = target_path_env(self.prefix_dir,
                                           self.cross_prefix_dir)
        self.environment['SED'] = 'sed'

        # in libitm method-serial.cc
        self.environment['CFLAGS'] += ' -Wno-unused-variable'
        self.environment['CXXFLAGS'] += ' -Wno-unused-variable'

        self.extract_dir = os.path.join(self.base_extract_dir,
                                        'gcc-%s' % (self.version))
        self.directory = os.path.join(self.base_extract_dir,
                                      'gcc-%s-build' % (self.version))

        self.install_args = ['make',
                             'install',
                             'MAKEINFO=true'
                             ]
        GccPrereqRecipesMixin.__init__(self, *args, **kwargs)

    def need_configure(self):
        return True

    def clean(self):
        if os.path.exists(self.extract_dir):
            shutil.rmtree(self.extract_dir)
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        super(GccPrereqRecipesMixin, self).clean()

    def compile(self):
#        dir = self.directory
#        self.directory = os.path.join(self.directory, 'gcc')
#        self.compile_args = ['make', 'params.list']
#        super(GccRecipe, self).compile()

        self.compile_args = ['make',
                             '-j%s' % self.cpu_count,
                             'MAKEINFO=true'
                             ]
#        self.directory = dir
        super(GccRecipe, self).compile()

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
        lib_dir = os.path.join(self.prefix_dir,
                               self.target_triplet, 'lib')
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

    def extract(self):
        super(GccRecipe, self).extract()

        # directory is not set until after extract
        from .glibc import GLibCRecipe
        glibc_version = GLibCRecipe().version
        check_directory(os.path.join(self.prefix_dir, 'include'))
        check_directory(os.path.join(self.prefix_dir, 'local'))
        self.configure_args = self.shell_args + [
            '%s/configure' % self.extract_dir,
            '--build=%s' % (self.target_triplet),
            '--host=%s' % (self.target_triplet),
            '--target=%s' % (self.target_triplet),
            '--prefix=%s' % (self.prefix_dir),
            '--with-local-prefix=%s/%s/local' % (
                self.cross_prefix_dir,
                self.target_triplet),
            '--with-native-system-header-dir=%s/%s/include' % (
                self.cross_prefix_dir,
                self.target_triplet),
            '--enable-languages=c,c++,fortran,objc,lto,obj-c++',
            '--enable-threads=posix',
            '--enable-__cxa_atexit',
            '--enable-clocale=gnu',
            '--enable-libssp',
            '--enable-lto',
            '--enable-libstdcxx-threads',
            '--disable-multilib',
            '--disable-nls',
            '--with-glibc-version=%s' % (glibc_version),
            'gcc_cv_libc_provides_ssp=yes',
            'glibcxx_cv_sys_sdt_h=no',
            ]
        check_directory(self.directory)

    def _patch_lib64(self):
        self.log_dir('patch', self.directory, 'lib to lib64')
        filename = os.path.join(self.extract_dir,
                                'gcc', 'config', 'i386', 't-linux64')
        src = 'm64=../lib64'
        dst = 'm64=../lib'
        patch(filename, src, dst)

    def patch(self):
#        self._patch_lib64()

        self.log_dir('patch', self.directory, 'creating libgcc link')
        src = os.path.join(self.cross_prefix_dir, 'lib')
        dst = os.path.join(self.prefix_dir, 'lib')
        if not os.path.exists(dst):
            os.makedirs(dst)
        files = ['libgcc_s.so', 'libgcc_s.so.1',
                 'libstdc++.so', 'libstdc++.so.6']
        for file in files:
            os.symlink(os.path.join(src, file),
                       os.path.join(dst, file))

        self.log_dir('patch', self.directory, 'creating lib64 symlink')
        lib = os.path.join(self.prefix_dir, self.target_triplet, 'lib')
        if not os.path.exists(lib):
            os.makedirs(lib)
        lib64 = os.path.join(self.prefix_dir, self.target_triplet, 'lib64')
        if not os.path.exists(lib64):
            os.symlink(lib, lib64)
#        cmd = self.shell_args + [
#               'contrib/download_prerequisites'
#               ]
#        self.run_exe(cmd, self.extract_dir, self.environment)

        super(GccPrereqRecipesMixin, self).patch()

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

    def post_install(self):
#        self.patch_limits()

        config = '%s/%s/include/c++/%s/bits/c++config.h' % \
            (self.prefix_dir, self.target_triplet, self.version)
        if os.path.exists(config):
            os.remove(config)

        dir = self.install_directory()

        # update ld.so.conf
        ld_so_conf = '''
$prefix/$target/lib64
$prefix/$target/lib
$prefix/lib64
$prefix/lib
$prefix/lib64/R/lib
'''
        ld_so_conf = Template(ld_so_conf).substitute(
            prefix=self.prefix_dir,
            target=self.target_triplet)
        etc_dir = os.path.join(self.prefix_dir, self.target_triplet, 'etc')
        with open(os.path.join(etc_dir, 'ld.so.conf'), 'wt') as f:
            f.write(ld_so_conf)

        self.log('post-install', 'update ld.so.cache')
        # update ld.so.cache
        args = ['../sbin/ldconfig',
                '-f', 'ld.so.conf'
                ]
        self.log('post-install', '(%s) %s' %
                 (etc_dir, ' '.join(args)))
        self.run_exe(args, etc_dir, self.environment)

        libnss_file = 'libnss_vas4.so.2'
        libnss_vas4 = '/lib64/%s' % (libnss_file)
        if os.path.exists(libnss_vas4):
            args = ['cp',
                    libnss_vas4,
                    '%s/%s/lib/%s' % (self.prefix_dir,
                                      self.target_triplet,
                                      libnss_file)
                    ]
            self.log('post-install', '(%s) %s' %
                     (dir, ' '.join(args)))
            self.run_exe(args, dir, self.environment)

        module_path = os.path.abspath(os.path.dirname(hardhat.__file__))
        symlinker = os.path.join(module_path, 'scripts', 'symlinker.sh')
        symlinker_dest = os.path.join(self.prefix_dir, 'bin', 'symlinker.sh')
        self.log('post-install', 'copying symlinker from %s to %s'
                 % (symlinker, symlinker_dest))
        shutil.copy2(symlinker, symlinker_dest)
        mode = stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH
        mode = mode | stat.S_IXOTH
        os.chmod(symlinker_dest, mode)

        dirs = ['etc',
                'include',
                'lib',
                'lib64',
                'sbin',
                'share',
                'var'
                ]

        self.log('post-install', 'symlinking directories')
        for dir in dirs:
            args = [
                symlinker_dest,
                '%s/%s/%s' % (self.prefix_dir, self.target_triplet, dir),
                '%s/%s' % (self.prefix_dir, dir)
                ]
            self.log('post-install', '(%s) %s' %
                     (self.prefix_dir, ' '.join(args)))
            self.run_exe(args, self.prefix_dir, self.environment)
        exes = [
            'addr2line',
            'ar',
            'as',
            'c++',
            'c++filt',
            'cpp',
            'elfedit',
            'g++',
            'gcc',
            'gcc-%s' % (self.version),
            'gcc-ar',
            'gcc-nm',
            'gcc-ranlib',
            'gcov',
            'gcov-tool',
            'gprof',
            'gfortran',
            'ld',
            'ld.bfd',
            'lipo',
            'nm',
            'objcopy',
            'objdump',
            'ranlib',
            'readelf',
            'size',
            'strings',
            'strip'
            ]

        self.log('post-install', 'symlinking executables')
        for exe in exes:
            src = os.path.join(self.prefix_dir,
                               'bin',
                               '%s-%s' % (self.target_triplet, exe))
            dst = os.path.join(self.prefix_dir,
                               'bin',
                               '%s' % (exe))

            self.log('post-install', 'symlinking %s to %s' % (src, dst))
            if not os.path.exists(dst):
                os.symlink(src, dst)

        cc = os.path.join(self.prefix_dir, 'bin', 'cc')
        gcc = os.path.join(self.prefix_dir, 'bin', 'gcc')
        if not os.path.exists(cc):
            os.symlink(gcc, cc)

        self.log_dir('post-install', self.directory, 'copy cpp')
        src = os.path.join(self.prefix_dir, 'bin', 'cpp')
        dst = os.path.join(self.prefix_dir, 'bin',
                           '%s-cpp' % self.target_triplet)
        if not os.path.exists(dst):
            shutil.copy2(src, dst)

    def patch_limits(self):
        # patch before and after build in case gcc updates to a wrong value
        self.log('patch', 'update gcc limits headers')
        args = ['/bin/bash',
                '--noprofile',
                '--norc',
                '-c',
                '"cat gcc/limitx.h gcc/glimits.h gcc/limity.h >'
                + ' `dirname $(%s-gcc -print-libgcc-file-name)`'
                % (self.target_triplet)
                + '/include-fixed/limits.h"'
        ]
        dir = os.path.join(os.path.dirname(self.install_directory()),
                           'gcc-%s' % (self.version))

        self.log_dir('patch', dir, ' '.join(args))
#        env = target_path_env(self.prefix_dir)
        self.run_exe(args, dir, self.environment)
