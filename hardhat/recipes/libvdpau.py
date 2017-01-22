from .base import GnuRecipe


class LibVdPauRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibVdPauRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '857a01932609225b9a3a5bf222b85e39' \
                      'b55c08787d0ad427dbd9ec033d58d736'

        self.name = 'libvdpau'
        self.version = '1.1.1'
        self.depends = ['doxygen', 'graphviz', 'texlive', 'xorg-libs']
        self.url = 'http://people.freedesktop.org/~aplattner/vdpau/' \
                   'libvdpau-$version.tar.bz2'
