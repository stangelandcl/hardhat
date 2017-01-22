from .base import GnuRecipe


class LibVaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibVaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '22bc139498065a7950d966dbdb000cad' \
                      '04905cbd3dc8f3541f80d36c4670b9d9'

        self.name = 'libva'
        self.version = '1.7.3'
        self.depends = ['doxygen', 'mesa', 'wayland']
        self.url = 'http://www.freedesktop.org/software/vaapi/releases/' \
                   'libva/libva-$version.tar.bz2'
