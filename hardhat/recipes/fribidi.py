from .base import GnuRecipe


class FriBidiRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FriBidiRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '08222a6212bbc2276a2d55c3bf370109' \
                      'ae4a35b689acbc66571ad2a670595a8e'

        self.name = 'fribidi'
        self.version = '0.19.7'
        self.depends = ['glib']
        self.url = 'http://fribidi.org/download/fribidi-$version.tar.bz2'
