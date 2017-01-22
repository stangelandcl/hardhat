from .base import SetupPyRecipe


class ZstdRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(ZstdRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '073cb0841f698c260401a9660a2b8958' \
                      'f46b9b8eb47bd186dbdf9418a24bfc4f'

        self.depends = ['zstd']
        self.name = 'zstd'
        self.version = '1bc5b7cacbd77abfa4157005845c730c46bd4b72'
        self.url = 'https://github.com/stangelandcl/python-zstd/archive/' \
                   '$version.tar.gz'
