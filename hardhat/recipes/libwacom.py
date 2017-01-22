from .base import GnuRecipe


class LibWacomRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibWacomRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f15d8e4f3bf3a5b2db0b3f9c9565361b' \
                      '084896c3cb54ac11b8de5e405f9cb045'

        self.name = 'libwacom'
        self.version = '0.34.0'
        self.depends = ['xorg-apps', 'xorg-libs']
        self.url = 'http://downloads.sourceforge.net/linuxwacom/' \
                   'xf86-input-wacom/xf86-input-wacom-$version.tar.bz2'
