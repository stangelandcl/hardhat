from .base import GnuRecipe


class LibGit2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibGit2Recipe, self).__init__(*args, **kwargs)
        self.name = 'libgit2'
        self.version = '0.24.1'
        self.url = 'https://github.com/libgit2/libgit2/archive/' \
                   'v$version.tar.gz'
