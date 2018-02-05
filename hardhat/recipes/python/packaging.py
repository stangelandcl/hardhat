from .base import PipBaseRecipe


class PackagingRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PackagingRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5d50835fdf0a7edf0b55e311b7c88778' \
                      '6504efea1177abd7e69329a8e5ea619e'
        self.name = 'packaging'
        self.version = '16.8'
        self.pydepends = ['pyparsing']
