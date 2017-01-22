from .base import GnuRecipe


class ByaccRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ByaccRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '178e08f7ab59edfb16d64902b7a9d785' \
                      '92d2d8d3ee30ab7a967188d969589b5a'

        self.name = 'byacc'
        self.version = '20160324'
        self.url = 'ftp://invisible-island.net/byacc/byacc-$version.tgz'
