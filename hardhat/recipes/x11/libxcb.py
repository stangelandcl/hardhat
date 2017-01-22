from ..base import GnuRecipe


class LibXcbRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXcbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4adfb1b7c67e99bc9c2ccb110b2f1756' \
                      '86576d2f792c8a71b9c8b19014057b5b'

        self.name = 'libxcb'
        self.version = '1.12'
        self.url = 'https://xcb.freedesktop.org/dist/libxcb-$version.tar.bz2'
        self.depends = ['libXau', 'pthread-stubs', 'util-macros', 'xcb-proto']
