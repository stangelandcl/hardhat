from .base import GnuRecipe


class JsonCRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JsonCRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5d867baeb7f540abe8f3265ac18ed7a2' \
                      '4f91fe3c5f4fd99ac3caba0708511b90'

        self.name = 'json-c'
        self.version = '0.13.1-20180305'
        self.depends = ['autoconf']
        self.url = 'https://github.com/json-c/json-c/archive/' \
                   'json-c-$version.tar.gz'

        self.environment['CFLAGS'] += ' -Wno-error=unused-but-set-variable'
        self.environment['CXXFLAGS'] = self.environment['CFLAGS']
        self.configure_strip_cross_compile()
