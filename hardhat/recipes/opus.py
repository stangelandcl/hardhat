from .base import GnuRecipe


class OpusRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpusRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '58b6fe802e7e30182e95d0cde890c0ac' \
                      'e40b6f125cffc50635f0ad2eef69b633'

        self.name = 'opus'
        self.version = '1.1.3'
        self.depends = ['doxygen', 'texlive']
        self.url = 'http://downloads.xiph.org/releases/opus/' \
                   'opus-$version.tar.gz'
