import os
import shutil
import stat
from string import Template
import hardhat
from hardhat.recipes.base import Configure, Make, MakeInstall, Recipe
from hardhat.util import check_directory, patch
from hardhat.environment import clean_env, target_path_env
from .gcc_pass1 import GccRecipe


class LibStdCppRecipe(Configure, Make, MakeInstall, Recipe):
    def __init__(self, *args, **kwargs):
        super(LibStdCppRecipe, self).__init__(*args, **kwargs)

        self.name = 'libstdc++'
        pass1 = GccRecipe(settings=self)
        self.version = pass1.version
        self.extract_dir = pass1.extract_dir
#        self.environment = clean_env(self.prefix_dir)

        self.configure_args = self.shell_args + [
            '%s/libstdc++-v3/configure' % (self.extract_dir),
            '--target=%s' % (self.target_triplet),
            '--host=%s' % (self.target_triplet),
            '--prefix=%s' % (self.prefix_dir),
            '--with-sysroot=%s' % (self.prefix_dir),
            '--with-gnu-as',
            '--with-gnu-ld',
            '--with-local-prefix=/local',
            '--with-native-system-header-dir=/include',
            '--with-gxx-include-dir=%s/%s/include/c++/%s' %
            (self.prefix_dir, self.target_triplet, self.version),
            '--disable-multilib',
            '--disable-nls',
            '--disable-libstdcxx-threads',
            '--disable-libstdcxx-pch',
            '--disable-maintainer-mode',
            'glibcxx_cv_sys_sdt_h=no',
            ]

        #  static link, from https://gcc.gnu.org/ml/gcc/2003-10/msg00606.html
        # add LDFLAGS=-static to statically compile
        self.compile_args += ['MAKEINFO=true']
        self.install_args += ['MAKEINFO=true']

    def clean(self):
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)

    def configure(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        super(LibStdCppRecipe, self).configure()


    def post_install(self):
        pass  # skip ldconfig
