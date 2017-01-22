from .base import GnuRecipe


class PintaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PintaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f1ea9e95f1051b92c8d8b6f622dfb77b' \
                      'd26254a165a836ec179aae10eb99d881'

        self.name = 'pinta'
        self.version = '1.6'
        self.url = 'https://github.com/PintaProject/Pinta/releases/' \
                   'download/$version/pinta-$version.tar.gz'
