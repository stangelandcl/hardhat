from .base import GnuRecipe


class LibtoolRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibtoolRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e3bd4d5d3d025a36c21dd6af7ea818a2' \
                      'afcd4dfc1ea5a17b39d7854bcd0c06e3'

        self.name = 'libtool'
        self.version = '2.4.6'
        self.depends = ['m4']
        self.url = 'http://ftpmirror.gnu.org/libtool/libtool-%s.tar.gz' \
            % (self.version)
