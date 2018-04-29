from .base import GnuRecipe


class NasmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NasmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '63ec86477ad3f0f6292325fd89e1d93a' \
                      'ea2e2fd490070863f17d48f7cd387011'

        self.name = 'nasm'
        self.version = '2.13.03'
        self.url = 'https://www.nasm.us/pub/nasm/releasebuilds/$version/' \
                   'nasm-$version.tar.bz2'
