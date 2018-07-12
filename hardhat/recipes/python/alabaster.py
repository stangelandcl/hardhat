from .base import PipBaseRecipe


class AlabasterRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AlabasterRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b63b1f4dc77c074d386752ec4a8a7517' \
                      '600f6c0db8cd42980cae17ab7b3275d7'

        self.name = 'alabaster'
        self.version = '0.7.11'
