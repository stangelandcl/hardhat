from .base import PipBaseRecipe


class PyYamlRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyYamlRecipe, self).__init__(*args, **kwargs)

        self.name = 'pyyaml'
        self.version = '3.12'
