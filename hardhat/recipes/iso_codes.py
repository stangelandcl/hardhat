from .base import GnuRecipe


class IsoCodesRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(IsoCodesRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'cbafd36cd4c588a254c0a5c42e682190' \
                      'c3784ceaf2a098da4c9c4a0cbc842822'

        self.name = 'iso-codes'
        self.version = '3.79'
        self.depends = ['python3']
#        self.url = 'https://pkg-isocodes.alioth.debian.org/downloads/' \
#                   'iso-codes-$version.tar.xz'
        self.url = 'http://anduin.linuxfromscratch.org/BLFS/iso-codes/' \
                   'iso-codes-$version.tar.xz'
