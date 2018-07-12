from .base import PipBaseRecipe


class PyYamlRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyYamlRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3ef3092145e9b70e3ddd2c7ad59bdd02' \
                      '52a94dfe3949721633e41344de00a6bf'
        self.name = 'pyyaml'
        self.version = '3.13'
