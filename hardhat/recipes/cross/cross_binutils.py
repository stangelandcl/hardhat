import os
import shutil
from hardhat.environment import toolchain_lib_path
from hardhat.urls import Urls
from .base import CrossGnuRecipe
from ..toolchain.binutils import BinutilsRecipe


class CrossBinutilsRecipe(CrossGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossBinutilsRecipe, self).__init__(*args, **kwargs)
        binutils = BinutilsRecipe(settings=self)
        self.sha256 = binutils.sha256
        self.version = binutils.version

        self.name = 'cross-binutils'

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
            ]
        self.compile_args += ['MAKEINFO=true']
        self.install_args += ['MAKEINFO=true']

        if not os.path.exists(self.environment['TMPDIR']):
            os.makedirs(self.environment['TMPDIR'])

    def version_check(self):
        pass

    def configure(self):
        self.directory = os.path.join(self.directory, 'build')
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.makedirs(self.directory)
        super(CrossBinutilsRecipe, self).configure()

    def post_install(self):
        lib = os.path.join(self.cross_prefix_dir, 'lib')
        lib64 = lib + '64'
        os.makedirs(lib)
        os.symlink(lib, lib64)
        # no ldconfig updating
