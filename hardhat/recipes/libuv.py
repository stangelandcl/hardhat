from .base import GnuRecipe, SourceMixin


class LibUVRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibUVRecipe, self).__init__(*args, **kwargs)
        self.sha256 = r'ce3036d444c3fb4f9a9e2994bec1f4fa' \
                       '07872b01456998b422ce918fdc55c254'
        self.depends = ['autotools']
        self.name = 'libuv'
        self.version = '1.25.0'
        self.url = 'https://github.com/libuv/libuv/archive/v$version.tar.gz'
        self.version_url = 'https://github.com/libuv/libuv/releases/'
        self.version_regex = r'v(?P<version>\d+\.\d+\.\d+)\.tar\.gz'
        self.configure_args = [
            ['./autogen.sh'],
            self.configure_args]


class LibUVSourceRecipe(SourceMixin, LibUVRecipe):
    def __init__(self, *args, **kwargs):
        super(LibUVSourceRecipe, self).__init__(*args, **kwargs)
