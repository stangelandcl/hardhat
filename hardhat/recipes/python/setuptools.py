from .base import PipBaseRecipe


class SetupToolsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SetupToolsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '47881d54ede4da9c15273bac65f9340f' \
                      '8929d4f0213193fa7894be384f2dcfa6'
        self.name = 'setuptools'
        self.version = '40.2.0'
        self.pydepends = ['appdirs']
