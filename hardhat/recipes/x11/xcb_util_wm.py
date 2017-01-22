from ..base import GnuRecipe


class XcbUtilWmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XcbUtilWmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '28bf8179640eaa89276d2b0f1ce42851' \
                      '03d136be6c98262b6151aaee1d3c2a3f'
        self.name = 'xcb-util-wm'
        self.version = '0.4.1'
        self.url = 'http://xcb.freedesktop.org/dist/' \
                   'xcb-util-wm-$version.tar.bz2'
        self.depends = ['libxcb']
