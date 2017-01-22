from .base import PipBaseRecipe


class NbFormatRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(NbFormatRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '389a5b630a30539074f238a48fb98645' \
                      '92f63d611baccfa2ffaf14ffe239de06'

        self.name = 'nbformat'
        self.version = '4.2.0'
        self.pydepends = ['jsonschema']
