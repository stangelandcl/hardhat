from .base import PipBaseRecipe


class PyYamlRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyYamlRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '592766c6303207a20efc445587778322' \
                      'd7f73b161bd994f227adaa341ba212ab'

        self.name = 'pyyaml'
        self.version = '3.12'
