from .base import GnuRecipe


class Sdl2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Sdl2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'edc77c57308661d576e843344d8638e0' \
                      '25a7818bff73f8fbfab09c3c5fd092ec'

        self.name = 'sdl2'
        self.version = '2.0.8'
        self.version_regex = r'SDL2[-](?P<version>\d+\.\d+\.\d+)\.tar\.gz'
        self.version_url = 'http://www.libsdl.org/release/'
        self.depends = ['pcre', 'pkgconfig', 'xorg-libs', 'xz', 'zlib']
        self.url = 'http://www.libsdl.org/release/SDL2-$version.tar.gz'
