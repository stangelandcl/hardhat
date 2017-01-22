from .base import X11BaseRecipe


class LibFontEncRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibFontEncRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '70588930e6fc9542ff38e0884778fbc6' \
                      'e6febf21adbab92fd8f524fe60aefd21'

        self.name = 'libfontenc'
        self.version = '1.1.3'
        self.depends = ['zlib']
