from .base import GnuRecipe


class Sdl2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Sdl2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '442038cf55965969f2ff06d976031813' \
                      'de643af9c9edc9e331bd761c242e8785'

        self.name = 'sdl2'
        self.version = '2.0.5'
        self.depends = ['pcre', 'pkgconfig', 'xz', 'zlib']
        self.url = 'http://www.libsdl.org/release/SDL2-$version.tar.gz'
