from .base import GnuRecipe


class AlsaToolsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AlsaToolsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd69c4dc2fb641a974d9903e9eb78c94c' \
                      'b0c7ac6c45bae664f0c9d6c0a1593227'
        self.name = 'alsa-tools'
        self.version = '1.1.6'
        self.depends = ['alsa-lib', 'fltk', 'gtk2', 'gtk3']
        self.url = 'ftp://ftp.alsa-project.org/pub/tools/' \
                   'alsa-tools-$version.tar.bz2'
        self.version_regex = r'''alsa\-tools\-(?P<version>\d+\.\d+\.\d+)\.tar\.bz2'''
        self.version_url = 'http://www.mirrorservice.org/sites/' \
                           'ftp.alsa-project.org/pub/tools/'
