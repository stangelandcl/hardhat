import os
import shutil
from .base import GnuRecipe
from ..util import save_url

class LibGit2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibGit2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '60198cbb34066b9b5c1613d15c0479f6' \
                      'cd25f4aef42f7ec515cd1cc13a77fede'

        self.name = 'libgit2'
        self.depends = ['curl', 'http-parser', 'openssl', 'zlib']
        self.version = '0.24.1'
        self.url = 'https://github.com/libgit2/libgit2/archive/' \
                   'v$version.tar.gz'
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]

    def install(self):
        super(LibGit2Recipe, self).install()

        self.log_dir('install', self.directory, 'installing examples')
        src = os.path.join(self.directory, 'examples')
        dst = os.path.join(self.prefix_dir, 'doc', 'libgit2', 'examples')

        if os.path.exists(dst):
            shutil.rmtree(dst)

        shutil.copytree(src, dst)

        dst = os.path.join(self.prefix_dir, 'doc', 'libgit2', '101-samples.html')
        save_url('https://libgit2.github.com/docs/guides/101-samples/', dst)
