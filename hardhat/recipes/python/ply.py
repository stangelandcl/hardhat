from .base import SetupPyRecipe


class PlyRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(PlyRecipe, self).__init__(*args, **kwargs)

        self.name = 'ply'
        self.version = '3.8'
        self.url = 'http://www.dabeaz.com/ply/ply-3.8.tar.gz'
        self.sha256 = 'e7d1bdff026beb159c9942f7a17e102c' \
                      '375638d9478a7ecd4cc0c76afd8de0b8'
