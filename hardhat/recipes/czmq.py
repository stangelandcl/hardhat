from .base import GnuRecipe


class CzmqRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CzmqRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8bca39ab69375fa4e981daf87b3feae8' \
                      '5384d5b40cef6adbe9d5eb063357699a'

        self.name = 'czmq'
        self.description = 'high level zeromq C and C++ library'
        self.version = '3.0.2'
        self.depends = ['zeromq']
        self.url = 'https://github.com/zeromq/$name/releases/download/' \
                   'v$version/$name-$version.tar.gz'

        self.environment['CFLAGS'] += ' -Wno-error'
