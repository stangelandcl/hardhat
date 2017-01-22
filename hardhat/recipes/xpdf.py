from .base import GnuRecipe


class XpdfRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XpdfRecipe, self).__init__(*args, **kwargs)
        self.name = 'xpdf'
        self.version = '3.02'
        self.depends = ['lesstiff']
        self.url = 'http://gd.tuwien.ac.at/publishing/xpdf/' \
                   'xpdf-$version.tar.gz'
