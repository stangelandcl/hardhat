from .base import PipBaseRecipe


class BeautifulSoupRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(BeautifulSoupRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3c9474036afda9136aac6463def733f8' \
                      '1017bf9ef3510d25634f335b0c87f5e1'

        self.name = 'beautifulsoup'
        self.pypi_name = 'beautifulsoup4'
        self.version = '4.5.1'
