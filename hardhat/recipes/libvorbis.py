from .base import GnuRecipe


class LibVorbisRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibVorbisRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '54f94a9527ff0a88477be0a71c0bab09' \
                      'a4c3febe0ed878b24824906cd4b0e1d1'

        self.name = 'libvorbis'
        self.depends = ['libogg']
        self.version = '1.3.5'
        self.url = 'http://downloads.xiph.org/releases/vorbis/' \
                   'libvorbis-$version.tar.xz'
