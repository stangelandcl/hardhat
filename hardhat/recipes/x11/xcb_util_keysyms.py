from ..base import GnuRecipe


class XcbUtilKeySymsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XcbUtilKeySymsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0ef8490ff1dede52b7de533158547f8b' \
                      '454b241aa3e4dcca369507f66f216dd9'

        self.name = 'xcb-util-keysyms'
        self.version = '0.4.0'
        self.depends = ['libxcb']
        self.url = 'http://xcb.freedesktop.org/dist/xcb-util-keysyms-$version.tar.bz2'

