from .base import GnuRecipe


class IsoCodesRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(IsoCodesRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '41e2fbaec2ed57e767b94f175d0dcd31' \
                      'b627aeb23b75cd604605a6fb6109d61f'

        self.name = 'iso-codes'
        self.version = '3.70'
        self.depends = ['python3']
        self.url = 'https://pkg-isocodes.alioth.debian.org/downloads/' \
                   'iso-codes-$version.tar.xz'
