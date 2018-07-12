from .base import GnuRecipe


class FriBidiRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FriBidiRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '94bdfe553e004d8bd095b109e1826823' \
                      '11dd511740d5083326d1582f1df237be'
                
        self.name = 'fribidi'
        self.version = '1.0.4'
        self.depends = ['glib']
        self.url = 'https://github.com/fribidi/fribidi/releases/download/v$version/fribidi-$version.tar.bz2'
