from .base import GnuRecipe


class XTermRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XTermRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '66fb2f6c35b342148f549c276b12a3aa' \
                      '3fb408e27ab6360ddec513e14376150b'

        self.name = 'xterm'
        self.version = '327'
        self.depends = ['xorg-libs']
        self.url = 'ftp://invisible-island.net/xterm/xterm-$version.tgz'
        self.environment['LIBS'] += ' -ltinfow'
