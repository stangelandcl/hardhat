from .base import PipBaseRecipe


class ConstantlyRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ConstantlyRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '586372eb92059873e29eba4f9dec8381' \
                      '541b4d3834660707faf8ba59146dfc35'
        self.pythons = ['python3']
        self.name = 'constantly'
        self.version = '15.1.0'
