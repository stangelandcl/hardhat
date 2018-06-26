from .base import GnuRecipe


class StraceRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(StraceRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '068cd09264c95e4d591bbcd3ea08f99a' \
                      '693ed8663cd5169b0fdad72eb5bdb39d'                                        
        self.name = 'strace'
        self.version = '4.22'
        self.url = 'https://github.com/strace/strace/releases/' \
                   'download/v$version/strace-$version.tar.xz'
