from .base import GnuRecipe


class AlsaToolsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AlsaToolsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7d34558c590a50294b36576d257316a1' \
                      'ac5cd951eb8cd7d330e09f8cc757ab51'

        self.name = 'alsa-tools'
        self.version = '1.1.0'
        self.depends = ['alsa-lib', 'fltk', 'gtk2', 'gtk3']
        self.url = 'ftp://ftp.alsa-project.org/pub/tools/' \
                   'alsa-tools-$version.tar.bz2'
