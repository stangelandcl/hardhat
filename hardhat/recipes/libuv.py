from .base import GnuRecipe, SourceMixin


class LibUVRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibUVRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '17afc94ec307be28fe8d431667917121' \
                      '9770df4f993905a79643c7583e106489'

        self.depends = ['autotools']
        self.name = 'libuv'
        self.version = '1.15.0'
        self.url = 'https://github.com/libuv/libuv/archive/v$version.tar.gz'
        self.configure_args = [
            ['./autogen.sh'],
            self.configure_args]


class LibUVSourceRecipe(SourceMixin, LibUVRecipe):
    def __init__(self, *args, **kwargs):
        super(LibUVSourceRecipe, self).__init__(*args, **kwargs)
