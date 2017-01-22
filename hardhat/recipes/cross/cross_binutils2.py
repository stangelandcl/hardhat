import os
import shutil
from hardhat.environment import toolchain_lib_path
from hardhat.urls import Urls
from .base import CrossGnuRecipe
from ..toolchain.binutils import BinutilsRecipe


class CrossBinutils2Recipe(CrossGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossBinutils2Recipe, self).__init__(*args, **kwargs)
        binutils = BinutilsRecipe(settings=self)
        self.sha256 = binutils.sha256
        self.version = binutils.version
        self.name = 'cross-binutils2'
        self.url = Urls.gnu_template('binutils', self.version)
        lib_paths = toolchain_lib_path(self.cross_prefix_dir,
                                       self.target_triplet)

        self.configure_args = self.shell_args + [
            '../configure',
            '--prefix=%s' % (self.cross_prefix_dir),
            '--with-lib-path=%s' % (lib_paths),
            '--target=%s' % (self.target_triplet),
            '--disable-nls',
            '--disable-werror'
#            '--with-sysroot'
            ]
        self.compile_args += ['MAKEINFO=true']
        self.install_args += ['MAKEINFO=true']

        self.environment['CC'] = self.target_triplet + '-gcc'
        self.environment['CXX'] = self.target_triplet + '-g++'
        self.environment['AR'] = self.target_triplet + '-ar'
        self.environment['LD'] = self.target_triplet + '-ld'
        self.environment['RANLIB'] = self.target_triplet + '-ranlib'
        self.environment['PATH'] = self.cross_prefix_dir + '/bin:' + \
            self.environment['PATH']
        self.environment['LIBRARY_PATH'] = os.path.join(
            self.cross_prefix_dir,
            self.target_triplet,
            'lib64')

    def version_check(self):
        pass

    def configure(self):
        self.directory = os.path.join(self.directory, 'build')
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.makedirs(self.directory)
        super(CrossBinutils2Recipe, self).configure()

    def post_install(self):
        pass
