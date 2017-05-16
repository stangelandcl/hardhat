from .base import PipBaseRecipe


class TranslationStringRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(TranslationStringRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4ee44cfa58c52ade8910ea0ebc3d2d84' \
                      'bdcad9fa0422405b1801ec9b9a65b72d'
                
        self.name = 'translationstring'
        self.version = '1.3'
