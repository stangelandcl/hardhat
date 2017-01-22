from .base import GnuRecipe


class LibdrmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibdrmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd80dd5a76c401f4c8756dcccd999c63d' \
                      '7e0a3bad258d96a829055cfd86ef840b'

        self.name = 'libdrm'
        self.version = '2.4.74'
        self.depends = ['xorg-libs']
        self.url = 'http://dri.freedesktop.org/libdrm/libdrm-$version.tar.bz2'
