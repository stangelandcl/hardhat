from .base import GnuRecipe


class YasmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(YasmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3dce6601b495f5b3d45b59f7d2492a34' \
                      '0ee7e84b5beca17e48f862502bd5603f'
        self.name = 'yasm'
        self.version = '1.3.0'
        self.url = 'http://www.tortall.net/projects/yasm/releases/' \
                   '$name-$version.tar.gz'
