from .base import PipBaseRecipe


class Meld3Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Meld3Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f7b754a0fde7a4429b2ebe49409db240' \
                      'b5699385a572501bb0d5627d299f9558'

        self.name = 'meld3'
        self.version = '1.0.2'
