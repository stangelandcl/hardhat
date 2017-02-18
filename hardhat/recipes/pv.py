from .base import GnuRecipe


class PVTimeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PVTimeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0ece824e0da27b384d11d1de371f20ca' \
                      'fac465e038041adab57fcf4b5036ef8d'

        self.description = 'pipe progress viewing'
        self.name = 'pv'
        self.version = '1.6.0'
        self.url = 'http://www.ivarch.com/programs/sources/pv-$version.tar.bz2'
