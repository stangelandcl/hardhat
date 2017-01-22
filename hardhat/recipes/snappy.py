from .base import GnuRecipe


class SnappyRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SnappyRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2f1e82adf0868c9e26a5a7a3115111b6' \
                      'da7e432ddbac268a7ca2fae2a247eef3'

        self.name = 'snappy'
        self.version = '1.1.3'
        self.version_url = 'https://github.com/google/snappy/releases'
        self.url = 'https://github.com/google/snappy/releases/download/' \
                   '$version/snappy-$version.tar.gz'
