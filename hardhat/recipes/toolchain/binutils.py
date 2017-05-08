import os
from hardhat.recipes.base import GnuRecipe
from hardhat.environment import target_path_env, toolchain_lib_path
from hardhat.urls import Urls
from hardhat.recipes.cross.base import CrossGnuRecipe


class BinutilsRecipe(CrossGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BinutilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = self.binutils_sha256
        self.name = 'binutils'
        self.version = self.binutils_version
        self.url = Urls.gnu_template(self.name, self.version)
        lib_paths = toolchain_lib_path(self.prefix_dir,
                                       self.target_triplet)
        self.configure_args = self.shell_args + [
            './configure',
            '--prefix=%s' % (self.prefix_dir),
#            '--with-sysroot=%s' % (self.prefix_dir),
            '--target=%s' % (self.target_triplet),
#            '--build=%s' % (self.target_triplet),
#            '--host=%s' % (self.target_triplet),
            '--with-lib-path=%s' % (lib_paths),
            '--enable-lto',
            '--enable-plugin',
            '--disable-multilib'
            ]
        self.compile_args += ['MAKEINFO=true']
        self.install_args += ['MAKEINFO=true']
        self.environment = target_path_env(self.cross_prefix_dir)
        self.environment['CFLAGS'] = '-O2'
        self.environment['CC'] = self.target_triplet + '-gcc'
        self.environment['CXX'] = self.target_triplet + '-g++'
        self.environment['AR'] = self.target_triplet + '-ar'
        self.environment['LD'] = self.target_triplet + '-ld'
        self.environment['RANLIB'] = self.target_triplet + '-ranlib'
        self.environment['LIBRARY_PATH'] = os.path.join(
            self.prefix_dir,
            self.target_triplet,
            'lib64')
#        self.environment['CPP'] = '/usr/bin/cpp'
#        self.environment['CC'] = '/usr/bin/gcc'
#        self.environment['CXX'] = '/usr/bin/g++'

    def post_install(self):
        pass  # no ldconfig updating
