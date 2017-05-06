from .base import GnuRecipe


class CAresRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CAresRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8692f9403cdcdf936130e045c8402166' \
                      '5118ee9bfea905d1a76f04d4e6f365fb'

        self.name = 'c-ares'
        self.version = '1.12.0'
        self.url = 'https://c-ares.haxx.se/download/$name-$version.tar.gz'
