from .base import PipBaseRecipe


class PackagingRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PackagingRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f019b770dd64e585a99714f1fd5e01c7' \
                      'a8f11b45635aa953fd41c689a657375b'

        self.name = 'packaging'
        self.version = '17.1'
        self.pydepends = ['pyparsing']
