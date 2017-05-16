from .base import PipBaseRecipe


class ApiPkgRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ApiPkgRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2e38399dbe842891fe85392601aab8f4' \
                      '0a8f4cc5a9053c326de35a1cc0297ac6'
                
        self.name = 'apipkg'
        self.version = '1.4'


