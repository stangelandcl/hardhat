from .base import GnuRecipe


class NeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ec4f5d919c38b1a5938b609a722d0d88' \
                      'a68c404b4564e3bb654b96b30582add9'

        self.name = 'ne'
        self.description = 'console text editor'
        self.version = '3.1.1'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/vigna/ne/releases'
        self.url = 'http://ne.di.unimi.it/ne-$version.tar.gz'
        self.compile_args += ["'LIBS=-lncursesw -ltinfow'"]
        self.install_args += ['PREFIX=%s' % self.prefix_dir]

    def configure(self):
        pass
