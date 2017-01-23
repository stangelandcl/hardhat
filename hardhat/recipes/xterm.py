from .base import GnuRecipe


class XTermRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XTermRecipe, self).__init__(*args, **kwargs)
        self.name = 'xterm'
        self.version = '327'
        self.depends = ['xorg-libs']
        self.url = 'ftp://invisible-island.net/xterm/xterm-$version.tgz'
