from ..base import GnuRecipe


class XcbUtilRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XcbUtilRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '46e49469cb3b594af1d33176cd7565de' \
                      'f2be3fa8be4371d62271fabb5eae50e9'

        self.name = 'xcb-util'
        self.version = '0.4.0'
        self.url = 'http://xcb.freedesktop.org/dist/xcb-util-$version.tar.bz2'
        self.depends = ['libxcb']
