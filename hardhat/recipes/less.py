from .base import GnuRecipe


class LessRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LessRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3fa38f2cf5e9e040bb44fffaa6c76a84' \
                      '506e379e47f5a04686ab78102090dda5'

        self.name = 'less'
        self.version = '481'
        self.url = 'http://www.greenwoodsoftware.com/less/less-$version.tar.gz'
        self.depends = ['ncurses']

