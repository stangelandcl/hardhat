import os
import platform
import shutil
from hardhat.recipes.base import GnuRecipe
from hardhat.util import check_directory
from hardhat.environment import target_path_env
from hardhat.recipes.cross.base import CrossGnuRecipe


class GLibCRecipe(CrossGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GLibCRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7e01959a42d37739e40d8ce58f9c1475' \
                      '0cc68bc8a8669889ed586f9f03b91fbe'
        self.name = 'glibc'
        self.version = '2.24'
        self.url = 'http://ftp.wayne.edu/gnu/libc/glibc-%s.tar.gz' \
            % (self.version)

        self.directory = os.path.join(self.base_extract_dir,
                                      'glibc-%s-build' % (self.version))

        self.environment = target_path_env(self.prefix_dir,
                                           self.cross_prefix_dir)


    def clean(self):
        if os.path.exists(self.extract_dir):
            shutil.rmtree(self.extract_dir)
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)

    def need_configure(self):
        return True

    def configure(self):
        check_directory(self.directory)
        super(GLibCRecipe, self).configure()

    def extract(self):
        super(GLibCRecipe, self).extract()

        prefix = os.path.join(self.prefix_dir, self.target_triplet)
        headers = os.path.join(self.prefix_dir, self.target_triplet, 'include')
        arch = platform.machine()

        # directory is not set until after extract
        self.configure_args = self.shell_args + [
            '%s/configure' % (self.extract_dir),
            '--prefix=%s' % (prefix),
            '--host=%s' % (self.target_triplet),
            '--target=%s' % (self.target_triplet),
#            '--build=%s' % (arch),
            '--with-headers=%s' % (headers),
            '--without-selinux',
            '--disable-multilib',
            '--enable-kernel=2.6.32',
            '--enable-obsolete-rpc',
#            'libc_cv_ssp=no',
#            'libc_cv_ssp_strong=no',
            ]

    def _replace(self, filename, src, dst):
        with open(filename, 'rt') as f:
            text = f.read()
        text = text.replace(src, dst)
        with open(filename, 'wt') as f:
            f.write(text)

    def post_install(self):
        # fix catchsegv libSegFault.so path
        target_base_dir = os.path.join(self.prefix_dir, self.target_triplet)
        file = os.path.join(target_base_dir, 'bin', 'catchsegv')
        self._replace(file, r'\$LIB', 'lib')


        # see here for emacs locale errors
        # http://unix.stackexchange.com/questions/195887/
        # emacs-text-mode-utf-8-characters
        dir = self.compile_directory()
        args = ['make',
                'localedata/install-locales'
                ]
        self.run_exe(args, dir, self.environment)


#        # update *.so paths to account for sysroot
#        lib_dir = os.path.join(target_base_dir, 'lib')
#        files = ['libc.so', 'libpthread.so', 'libm.so']
#
#        for file in files:
#            full = os.path.join(lib_dir, file)
#            self._replace(full, self.prefix_dir, '')




#        # The ldd scripts looks for ld-linux-x86-64.so.2 in the lib64
#        # directory. See: https://lists.gnu.org/archive/html/guix-devel/
#        # 2013-09/msg00138.html
#        # Or run sh -x ldd $(which ls) to see the paths it looks for
#        #
#        # Example dest path:
#        # $PREFIX/x86_64-srcinstall-linux-gnu/lib64/
#        # ld-linux-x86-64.so.2
#        ld_linux = 'ld-linux-x86-64.so.2'
#        src_file = os.path.join(target_base_dir, 'lib', ld_linux)
#        link_file = os.path.join(target_base_dir, 'lib64', ld_linux)
#        link_dir = os.path.dirname(link_file)
#        if not os.path.exists(link_dir):
#            os.makedirs(link_dir)
#        os.symlink(src_file, link_file)
