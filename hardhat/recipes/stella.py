from .base import GnuRecipe


class StellaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(StellaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e1507966e1b3d3a5fb81757dc82fba8c' \
                      'f546618ef3d2389773aca2a70a263478'

        self.description = 'Atari VCS emulator'
        self.name = 'stella'
        self.version = '5.1.3'
        self.depends = ['libpng', 'sdl2', 'zlib']
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)\.tar\.gz'
        self.version_url = 'https://github.com/stella-emu/stella/releases/'
        self.depends = ['autotools', 'pcre', 'pkgconfig', 'xz', 'zlib']
        self.url = 'https://github.com/stella-emu/stella/archive/$version.tar.gz'
        self.configure_strip_cross_compile()
