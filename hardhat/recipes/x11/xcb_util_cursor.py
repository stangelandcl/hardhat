from ..base import GnuRecipe


class XcbUtilCursorRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XcbUtilCursorRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '05a10a0706a1a789a078be297b5fb663' \
                      'f66a71fb7f7f1b99658264c35926394f'
        self.name = 'xcb-util-cursor'
        self.version = '0.1.3'
        self.url = 'https://xcb.freedesktop.org/dist/xcb-util-cursor-$version.tar.bz2'
        self.depends = ['libxcb', 'xcb-util-renderutil']


