from ..base import GnuRecipe


class XcbUtilRenderUtilRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XcbUtilRenderUtilRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c6e97e48fb1286d6394dddb1c1732f00' \
                      '227c70bd1bedb7d1acabefdd340bea5b'

        self.name = 'xcb-util-renderutil'
        self.version = '0.3.9'
        self.depends = ['libxcb']
        self.url = 'https://xcb.freedesktop.org/dist/xcb-util-renderutil-$version.tar.bz2'




