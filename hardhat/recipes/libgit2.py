from .base import GnuRecipe


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

