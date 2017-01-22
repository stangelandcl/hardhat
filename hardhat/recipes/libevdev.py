from .base import GnuRecipe


class LibEvDevRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibEvDevRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '320120782018b992956b3fa29495c323' \
                      '832860807ac8ea74537e636a0e0280b1'

        self.name = 'libevdev'
        self.version = '1.5.5'
        self.depends = ['check', 'doxygen', 'python3']
        self.url = 'http://www.freedesktop.org/software/libevdev/' \
                   'libevdev-$version.tar.xz'
