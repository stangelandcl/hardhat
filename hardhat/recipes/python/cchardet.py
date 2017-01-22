from .base import PipBaseRecipe


class CChardetRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CChardetRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0f757d0761d8d23b1071cae2110fa2a2' \
                      'dcd8e529655c495b5ee25dddb48f07bd'

        self.name = 'cchardet'
        self.version = '1.1.2'
