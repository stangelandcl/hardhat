from ..base import GnuRecipe


class UtilMacrosRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(UtilMacrosRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2835b11829ee634e19fa56517b4cfc52' \
                      'ef39acea0cd82e15f68096e27cbed0ba'

        self.name = 'util-macros'
        self.version = '1.19.0'
        self.url = 'http://ftp.x.org/archive/individual/util/' \
                   'util-macros-$version.tar.bz2'

    def compile(self):
        pass
