from .base import PipBaseRecipe


class PyYamlRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyYamlRecipe, self).__init__(*args, **kwargs)

        self.name = 'pyyaml'
        self.version = '3.11'
        self.sha256 = 'c36c938a872e5ff494938b33b14aaa156' \
                      'cb439ec67548fcab3535bb78b0846e8'
