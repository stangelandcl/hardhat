from .base import GnuRecipe


class LibdrmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibdrmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e9e48fdb4de139dc4d9880aa1473158a' \
                     '16ff6aff63d14341367bd30a51ff39fa'
        self.name = 'libdrm'
        self.version = '2.4.92'
        self.depends = ['xorg-libs']
        self.url = 'http://dri.freedesktop.org/libdrm/libdrm-$version.tar.bz2'
