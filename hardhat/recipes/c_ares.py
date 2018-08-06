from .base import GnuRecipe


class CAresRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CAresRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '45d3c1fd29263ceec2afc8ff9cd06d5f' \
                      '8f889636eb4e80ce3cc7f0eaf7aadc6e'
        self.name = 'c-ares'
        self.version = '1.14.0'
        self.url = 'https://c-ares.haxx.se/download/$name-$version.tar.gz'
