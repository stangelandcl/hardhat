import os
from .base import GnuRecipe


class CabalRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CabalRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c00e9d372adb49ce1bd5b62ff049cf49' \
                      'adc4a312a271b238894e50eb707297aa'

        self.name = 'cabal'
        self.depends = ['ghc']
        self.version = '1.24.0.0'
        self.url = 'https://www.haskell.org/cabal/release/cabal-$version/' \
                   'Cabal-$version.tar.gz'

        self.install_args = ['./Setup', 'install']

    def need_configure(self):
        return False

    def compile(self):
        self.compile_args = ['ghc', '-threaded', '--make', 'Setup']
        super(CabalRecipe, self).compile()
        self.compile_args = ['./Setup', 'configure', '--user',
                             '--prefix=%s/cabal' % self.prefix_dir]
        super(CabalRecipe, self).compile()
        self.compile_args = ['./Setup', 'build']
        super(CabalRecipe, self).compile()
