import os
import shutil
from .base import GnuRecipe


class Mingw64Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Mingw64Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '0c407394b0d8635553f4fbca674cdfe4' \
                      '46aac223e90b4010603d863e4bdd015c'

        self.name = 'mingw-w64'
        self.version = '4.0.6'
        self.url = 'http://downloads.sourceforge.net/project/mingw-w64/mingw-w64/mingw-w64-release/' \
                   'mingw-w64-v$version.tar.bz2'

        self.configure_strip_cross_compile()
        self.prefix_dir = os.path.join(self.prefix_dir, 'mingw64')
        self.configure_args += ['--build=%s' % self.target_triplet,
                                '--host=%s' % self.target_triplet,
                                '--with-tools=all']
        # See docs in mingw64-w64-doc/howto-build
        # This requires a multi stage building including binutils, and gcc in
        # multiple steps
