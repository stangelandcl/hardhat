from .base import GnuRecipe


class AlsaOssRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AlsaOssRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c3d3f743e61f05ff95c5cba3b06bc9c9' \
                      '1ff86c37495f1d19dab844e6b90845ea'
        self.name = 'alsa-oss'
        self.version = '1.1.6'
        self.depends = ['alsa-lib']
        self.url = 'ftp://ftp.alsa-project.org/pub/oss-lib/' \
                   'alsa-oss-$version.tar.bz2'
        self.version_regex = r'''alsa\-oss\-(?P<version>\d+\.\d+\.\d+)\.tar\.bz2'''
        self.version_url = 'http://www.mirrorservice.org/sites/' \
                           'ftp.alsa-project.org/pub/oss-lib/'
