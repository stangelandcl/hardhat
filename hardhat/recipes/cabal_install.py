import os
from .base import GnuRecipe


class CabalInstallRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CabalInstallRecipe, self).__init__(*args, **kwargs)
        self.name = 'cabal-install'
        self.version = '1.24.0.0'
        self.url = 'https://www.haskell.org/cabal/release/$name-$version/' \
                   '$name-$version.tar.gz'

        self.install_args = ['./Setup', 'install']

    def need_configure(self):
        return False

    def compile(self):
        self.compile_args = ['ghc', '-threaded', '--make', 'Setup']
        super(CabalInstallRecipe, self).compile()
        self.compile_args = ['./Setup', 'configure', '--user',
                             '--prefix=%s/cabal' % self.prefix_dir]
        super(CabalInstallRecipe, self).compile()
        self.compile_args = ['./Setup', 'build']
        super(CabalInstallRecipe, self).compile()
