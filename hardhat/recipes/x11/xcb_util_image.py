from ..base import GnuRecipe


class XcbUtilImageRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XcbUtilImageRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2db96a37d78831d643538dd1b595d7d7' \
                      '12e04bdccf8896a5e18ce0f398ea2ffc'
        self.name = 'xcb-util-image'
        self.version = '0.4.0'
        self.url = 'http://xcb.freedesktop.org/dist/' \
                   'xcb-util-image-$version.tar.bz2'
        self.depends = ['xcb-util']
