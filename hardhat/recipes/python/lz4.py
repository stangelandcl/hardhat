from .base import SetupPyRecipe


class Lz4Recipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(Lz4Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '7e77fdc06b541c8831e8de7c25f54050' \
                      '038bb4a60cc58ce981e74704f389f182'

        self.depends = ['lz4']
        self.name = 'lz4'
        self.version = '28f599e2d7b6c34e3136751480bf6786df568990'
        self.url = 'https://github.com/stangelandcl/python-lz4/archive/' \
                   '$version.tar.gz'
