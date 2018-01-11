from .base import GnuRecipe


class WineRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(WineRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '487131e69875ae9c2d042798f9541601' \
                      '46e603e449c3c97981f29b42f4a66095'

        self.name = 'wine'
        self.version = '2.19'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'http://dl.winehq.org/wine/source/2.x/'
        # requires flex != 2.6.3
        self.depends = ['autotools', 'flex']
        # optional dependencies: x11
        self.url = 'http://dl.winehq.org/wine/source/2.x/wine-$version.tar.xz'
        self.configure_args += ['--enable-win64',
                                '--without-x']
#        self.compile_args = ['make']
        self.configure_strip_cross_compile()
        self.environment_strip_lto()
