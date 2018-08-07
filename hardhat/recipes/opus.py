from .base import GnuRecipe


class OpusRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpusRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'cfafd339ccd9c5ef8d6ab15d7e1a412c' \
                      '054bf4cb4ecbbbcc78c12ef2def70732'
        self.name = 'opus'
        self.version = '1.2.1'
        self.depends = ['doxygen', 'texlive']
        self.url = 'http://downloads.xiph.org/releases/opus/' \
                   'opus-$version.tar.gz'
