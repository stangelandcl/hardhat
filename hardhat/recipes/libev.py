from .base import GnuRecipe


class LibEvRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibEvRecipe, self).__init__(*args, **kwargs)
        self.name = 'libev'
        self.version = '4.22'
        self.url = 'http://dist.schmorp.de/libev/libev-$version.tar.gz'
        self.sha256 = '736079e8ac543c74d59af73f9c52737b' \
                      '3bfec9601f020bf25a87a4f4d0f01bd6'
