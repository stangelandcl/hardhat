from .base import GnuRecipe


class PThreadStubsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PThreadStubsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '35b6d54e3cc6f3ba28061da81af64b9a' \
                      '92b7b757319098172488a660e3d87299'

        self.name = 'pthread-stubs'
        self.version = '0.3'
        self.url = 'https://xcb.freedesktop.org/dist/' \
                   'libpthread-stubs-$version.tar.bz2'
