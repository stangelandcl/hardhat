from .base import X11BaseRecipe


class XBitmapsRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(XBitmapsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3671b034356bbc4d32d052808cf646c9' \
                      '40ec8b2d1913adac51b1453e41aa1e9d'

        self.name = 'xbitmaps'
        self.depends = ['util-macros']
        self.version = '1.1.1'
        self.url = 'http://ftp.x.org/pub/individual/data/' \
                   '$name-$version.tar.bz2'
