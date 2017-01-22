from .base import GnuRecipe


class JsonCRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JsonCRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '000c01b2b3f82dcb4261751eb71f1b08' \
                      '4404fb7d6a282f06074d3c17078b9f3f'

        self.name = 'json-c'
        self.version = '0.12'
        self.depends = []
        self.url = 'https://s3.amazonaws.com/json-c_releases/releases/' \
                   'json-c-$version.tar.gz'

        self.environment['CFLAGS'] += ' -Wno-error=unused-but-set-variable'
        self.environment['CXXFLAGS'] = self.environment['CFLAGS']
        self.configure_strip_cross_compile()
