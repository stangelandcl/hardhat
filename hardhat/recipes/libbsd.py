from .base import GnuRecipe


class LibBsdRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibBsdRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '56d835742327d69faccd16955a60b6dc' \
                      'f30684a8da518c4eca0ac713b9e0a7a4'
        self.name = 'libbsd'
        self.version = '0.9.1'
        self.version_regex = r'libbsd\-(?P<version>\d+\.\d+\.\d+).\tar\.xz'
        self.version_url = 'https://github.com/ggreer/the_silver_searcher/' \
                           'releases'
        self.url = 'https://libbsd.freedesktop.org/releases/' \
                   'libbsd-$version.tar.xz'
