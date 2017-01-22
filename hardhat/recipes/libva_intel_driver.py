from .base import GnuRecipe


class LibVaIntelDriverRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibVaIntelDriverRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '76ad37d9fd5ae23d8ce6052d50b5e643' \
                      '8a8df9e769b13fe34b771cd453f4f937'

        self.name = 'libva-intel-driver'
        self.version = '1.7.3'
        self.depends = ['doxygen', 'libva', 'mesa', 'wayland']
        self.url = 'http://www.freedesktop.org/software/vaapi/releases/' \
                   'libva-intel-driver/libva-intel-driver-$version.tar.bz2'
