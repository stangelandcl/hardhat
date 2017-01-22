from .base import GnuRecipe


class AlsaLibRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AlsaLibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8ac76c3144ed2ed49da7622ab65ac541' \
                      '5205913ccbedde877972383cbc234269'

        self.name = 'alsa-lib'
        self.version = '1.1.1'
        self.url = 'ftp://ftp.alsa-project.org/pub/lib/' \
                   'alsa-lib-$version.tar.bz2'
        self.depends = ['python2']
        self.environment_strip_lto()
