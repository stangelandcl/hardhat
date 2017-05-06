from .base import GnuRecipe


class LibUVRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibUVRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6ec7eec6ecc24b1a8ffedebedb2fe931' \
                      '3fffb5410de89aaf784dd01080411c7a'
        self.depends = ['autotools']
        self.name = 'libuv'
        self.version = '1.11.0'
        self.url = 'https://github.com/libuv/libuv/archive/v$version.tar.gz'
        self.configure_args = [
            ['./autogen.sh'],
            self.configure_args]
