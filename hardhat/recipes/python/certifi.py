from .base import PipBaseRecipe


class CertifiRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CertifiRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '13e698f54293db9f89122b0581843a78' \
                      '2ad0934a4fe0172d2a980ba77fc61bb7'

        self.name = 'certifi'
        self.version = '2018.4.16'
