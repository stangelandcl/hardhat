from .base import GnuRecipe


class CAresRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CAresRecipe, self).__init__(*args, **kwargs)
        self.name = 'c-ares'
        self.version = '1.11.0'
        self.url = 'https://c-ares.haxx.se/download/$name-$version.tar.gz'
        self.sha256 = 'b3612e6617d9682928a1d50c1040de4d' \
                      'b6519f977f0b25d40cf1b632900b3efd'
