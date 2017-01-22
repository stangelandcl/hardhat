import os
from .base import GnuRecipe


class MakeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MakeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd6e262bf3601b42d2b1e4ef8310029e1' \
                      'dcf20083c5446b4b7aa67081fdffc589'

        self.name = 'make'
        self.version = '4.2.1'
        self.url = 'http://open-source-box.org/make/make-$version.tar.bz2'
        self.configure_args += ['--without-guile']

    def install(self):
        super(MakeRecipe, self).install()

        src = os.path.join(self.prefix_dir, 'bin', 'make')
        dst = os.path.join(self.prefix_dir, 'bin', 'gmake')
        if os.path.exists(dst):
            os.remove(dst)
        os.symlink(src, dst)
