from ..base import GnuRecipe


class XcbUtilXrmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XcbUtilXrmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '301cf33701207ea8782d49f4cb6404ab' \
                      'd8f2d64e16f242017fd720be7c900c85'
        self.name = 'xcb-util-xrm'
        self.version = '1.3'
        self.depends = ['libxcb']
        self.url = 'https://github.com/Airblader/xcb-util-xrm/releases/' \
                   'download/v$version/xcb-util-xrm-$version.tar.bz2'
