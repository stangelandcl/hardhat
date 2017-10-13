from .base import GnuRecipe


class WineRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(WineRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f71884f539928877f4b415309f582825' \
                      'd3d3c9976104e43d566944c710713c9a'

        self.name = 'wine'
        self.version = '2.0.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'http://dl.winehq.org/wine/source/2.0/'
        self.depends = ['autotools', 'x11']
        self.url = 'http://dl.winehq.org/wine/source/%s/wine-$version.tar.xz' \
            % '.'.join(self.version.split('.')[:2])
        self.configure_args += ['--enable-win64']
        self.compile_args = ['make']
        self.configure_strip_cross_compile()
        self.environment_strip_lto()
