from .base import GnuRecipe


class ExpatRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ExpatRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'aff584e5a2f759dcfc6d48671e9529f6' \
                      'afe1e30b0cd6a4cec200cbe3f793de67'
        self.name = 'expat'  # includes liblzma
        self.version = '2.1.1'
        self.url = 'https://downloads.sourceforge.net/project/expat/expat/' \
                   '$version/expat-$version.tar.bz2'
