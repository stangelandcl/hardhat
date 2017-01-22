from ..base import GnuRecipe


class XcbProtoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XcbProtoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5922aba4c664ab7899a29d92ea91a87a' \
                      'a4c1fc7eb5ee550325c3216c480a4906'

        self.name = 'xcb-proto'
        self.version = '1.12'
        self.url = 'https://xcb.freedesktop.org/dist/' \
                   'xcb-proto-$version.tar.bz2'
