from .base import GnuRecipe


class LibFakeTimeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibFakeTimeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '56bc32006f4c5b021ff648cc1fd458c5' \
                      '316f40aadfd2031879229a234189b031'
        self.name = 'libfaketime'
        self.version = '0.9.6'
        self.url = 'https://github.com/wolfcw/libfaketime/archive/' \
                   'v$version.tar.gz'
        self.environment['CFLAGS'] += ' -Wno-error=nonnull-compare'
