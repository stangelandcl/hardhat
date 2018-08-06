from .base import GnuRecipe


class AlsaUtilsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AlsaUtilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '155caecc40b2220f686f34ba3655a53e' \
                      '3bdbc0586adb1056733949feaaf7d36e'
        self.name = 'alsa-utils'
        self.version = '1.1.6'
        self.depends = ['alsa-lib']
        self.url = 'ftp://ftp.alsa-project.org/pub/utils/' \
                   'alsa-utils-$version.tar.bz2'
        self.version_regex = r'''alsa\-utils\-(?P<version>\d+\.\d+\.\d+)\.tar\.bz2'''
        self.version_url = 'http://www.mirrorservice.org/sites/' \
                           'ftp.alsa-project.org/pub/utils/'
        self.environment['NCURSESW_LIBS'] = '-lncursesw -ltinfow'
