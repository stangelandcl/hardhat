from .base import PipBaseRecipe


class CertifiRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CertifiRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'edbc3f203427eef571f79a7692bb160a' \
                      '2b0f7ccaa31953e99bd17e307cf63f7d'
        self.name = 'certifi'
        self.version = '2018.1.18'
