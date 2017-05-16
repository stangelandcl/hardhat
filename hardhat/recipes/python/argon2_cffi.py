from .base import PipBaseRecipe


class Argon2CffiRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Argon2CffiRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '99a5246d68fb17c33eddc9e8b21cfcb0' \
                      'de1f8360d0bb0b73be5ede20078de3aa'
                
        self.name = 'argon2_cffi'
        self.version = '16.3.0'
