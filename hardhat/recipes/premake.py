from .base import GnuRecipe


class PremakeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PremakeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6a71a47c3da137d72bfca9774a2c7447' \
                      '6ace111a423aa02f2e6a6be394c5838a'

        self.name = 'premake'
        self.version = '5.0.0-alpha9'
        self.url = 'https://github.com/premake/premake-core/releases/' \
                   'download/v$version/premake-$version-src.zip'
