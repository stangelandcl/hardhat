from .base import GnuRecipe


class SnappyRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SnappyRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '134bfe122fd25599bb807bb8130e7ba6' \
                      'd9bdb851e0b16efcb83ac4f5d0b70057'
        self.name = 'snappy'
        self.version = '1.1.4'
        self.version_url = 'https://github.com/google/snappy/releases'
        self.url = 'https://github.com/google/snappy/releases/download/' \
                   '$version/snappy-$version.tar.gz'
