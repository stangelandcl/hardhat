from .base import GnuRecipe


class SrmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SrmRecipe, self).__init__(*args, **kwargs)
        self.description = 'Secure delete rm'
        self.sha256 = '7583c1120e911e292f22b4a1d949b32c' \
                      '23518038afd966d527dae87c61565283'

        self.name = 'srm'
        self.version = '1.2.15'
        self.url = 'https://sourceforge.net/projects/srm/files/$version/' \
                   'srm-$version.tar.gz'
