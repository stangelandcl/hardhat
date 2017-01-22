from .base import GnuRecipe


class LibVdPauVaGlRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibVdPauVaGlRecipe, self).__init__(*args, **kwargs)
        self.name = 'libvdpau-va-gl'
        self.version = '0.4.0'
        self.depends = ['cmake', 'doxygen', 'graphviz', 'ffmpeg', 'libva',
                        'texlive']
        self.url = 'https://github.com/i-rinat/libvdpau-va-gl/archive/' \
                   'v$version.tar.gz'
