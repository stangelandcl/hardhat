from ..base import X11BaseRecipe


class XKeyboardConfigRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(XKeyboardConfigRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '83dfd186b9eb9ced69e01d8d8e2f15b6' \
                      'a79b2e30124874ef086f2d3048f45827'

        self.name = 'xkeyboard-config'
        self.version = '2.19'
        self.depends = ['xorg-libs']
        self.configure_args += ['--with-xkb-rules-symlink=xorg']
        self.url = 'http://www.x.org/releases/individual/data/' \
                   'xkeyboard-config/xkeyboard-config-$version.tar.bz2'
