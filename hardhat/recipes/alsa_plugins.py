from .base import GnuRecipe


class AlsaPluginsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AlsaPluginsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6f1d31ebe3b1fa1cc8dade60b7bed1cb' \
                      '2583ac998167002d350dc0a5e3e40c13'
        self.name = 'alsa-plugins'
        self.version = '1.1.6'
        self.depends = ['alsa-lib']
        self.url = 'ftp://ftp.alsa-project.org/pub/plugins/' \
                   'alsa-plugins-$version.tar.bz2'
        self.version_regex = r'''alsa\-plugins\-(?P<version>\d+\.\d+\.\d+)\.tar\.bz2'''
        self.version_url = 'http://www.mirrorservice.org/sites/' \
                           'ftp.alsa-project.org/pub/plugins/'
