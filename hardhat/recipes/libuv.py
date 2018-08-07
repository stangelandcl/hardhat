from .base import GnuRecipe, SourceMixin


class LibUVRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibUVRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c72f0401e1298f948daf310abafce383' \
                      '73a926fb9438464d1bf7fe90784544e0'
        self.depends = ['autotools']
        self.name = 'libuv'
        self.version = '1.22.0'
        self.url = 'https://github.com/libuv/libuv/archive/v$version.tar.gz'
        self.version_url = 'https://github.com/libuv/libuv/releases/'
        self.version_regex = r'v(?P<version>\d+\.\d+\.\d+)\.tar\.gz'
        self.configure_args = [
            ['./autogen.sh'],
            self.configure_args]


class LibUVSourceRecipe(SourceMixin, LibUVRecipe):
    def __init__(self, *args, **kwargs):
        super(LibUVSourceRecipe, self).__init__(*args, **kwargs)
