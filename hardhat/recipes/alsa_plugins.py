from .base import GnuRecipe


class AlsaPluginsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AlsaPluginsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8ea4d1e082c36528a896a2581e5eb62d' \
                      '4dc2683238e353050d0d624e65f901f1'

        self.name = 'alsa-plugins'
        self.version = '1.1.1'
        self.depends = ['alsa-lib']
        self.url = 'ftp://ftp.alsa-project.org/pub/plugins/' \
                   'alsa-plugins-$version.tar.bz2'
