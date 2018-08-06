from .base import GnuRecipe


class AlsaLibRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AlsaLibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5f2cd274b272cae0d0d111e8a9e363f0' \
                      '8783329157e8dd68b3de0c096de6d724'
        self.name = 'alsa-lib'
        self.version = '1.1.6'
        self.url = 'ftp://ftp.alsa-project.org/pub/lib/' \
                   'alsa-lib-$version.tar.bz2'
        self.version_regex = r'''alsa\-lib\-(?P<version>\d+\.\d+\.\d+)\.tar\.bz2'''
        self.version_url = 'http://www.mirrorservice.org/sites/' \
                           'ftp.alsa-project.org/pub/lib/'

        self.depends = ['python2']
        self.environment_strip_lto()
