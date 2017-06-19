from .base import GnuRecipe


class FuseRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FuseRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ec632de07b79ec72a591f9878a6d090c' \
                      '249bdafb4e2adf47fa46dc681737b205'

        self.name = 'fuse'
        self.version = '3.0.2'
        self.depends = ['autotools', 'pcre', 'pkgconfig', 'xz', 'zlib']
        self.url = 'https://github.com/libfuse/libfuse/releases/download/' \
                   'fuse-$version/fuse-$version.tar.gz'

        # TODO: install documentation
