from .base import PipBaseRecipe


class CythonRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CythonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1aae6d6e9858888144cea147eb5e6778' \
                      '30f45faaff3d305d77378c3cba55f526'
        self.name = 'cython'
        self.version = '0.28.3'
        self.pypi_name = 'Cython'
