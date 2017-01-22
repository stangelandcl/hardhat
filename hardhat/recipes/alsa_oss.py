from .base import GnuRecipe


class AlsaOssRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AlsaOssRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3ae62caa88a0bc7b30ed836dcb794dc6' \
                      'ef4d3650439e2260db54cace7d5c6ad5'

        self.name = 'alsa-oss'
        self.version = '1.0.28'
        self.depends = ['alsa-lib']
        self.url = 'ftp://ftp.alsa-project.org/pub/oss-lib/' \
                   'alsa-oss-$version.tar.bz2'
