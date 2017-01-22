from .base import GnuRecipe


class LibCanberraRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibCanberraRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c2b671e67e0c288a69fc33dc1b6f1b53' \
                      '4d07882c2aceed37004bf48c601afa72'

        self.name = 'libcanberra'
        self.depends = ['alsa-lib', 'gstreamer', 'libvorbis', 'gtk3']
        self.version = '0.30'
        self.url = 'http://0pointer.de/lennart/projects/libcanberra/' \
                   'libcanberra-$version.tar.xz'
