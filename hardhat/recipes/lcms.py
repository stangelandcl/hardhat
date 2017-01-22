from .base import GnuRecipe


class LcmsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LcmsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4524234ae7de185e6b6da5d31d687508' \
                      '5b2198bc63b1211f7dde6e2d197d6a53'
        self.description = 'Little CMS. Light color management system'
        self.name = 'lcms'
        self.version = '2.7'
        self.depends = ['libjpeg-turbo', 'libtiff']
        self.url = 'http://downloads.sourceforge.net/lcms/' \
                   'lcms2-$version.tar.gz'
