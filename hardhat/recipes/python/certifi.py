from .base import PipBaseRecipe


class CertifiRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CertifiRecipe, self).__init__(*args, **kwargs)
        self.name = 'certifi'
        self.version = '2018.1.18'
