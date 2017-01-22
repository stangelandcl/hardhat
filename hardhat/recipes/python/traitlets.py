from .base import PipBaseRecipe


class TraitletsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(TraitletsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ba8c94323ccbe8fd792e45d8efe8c95d' \
                      '3e0744cc8c085295b607552ab573724c'

        self.name = 'traitlets'
        self.pydepends = ['ipython-genutils']
        self.version = '4.3.1'
