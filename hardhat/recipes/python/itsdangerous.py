from .base import PipBaseRecipe


class ItsDangerousRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ItsDangerousRecipe, self).__init__(*args, **kwargs)

        self.name = 'itsdangerous'
        self.version = '0.24'
        self.sha256 = 'cbb3fcf8d3e33df861709ecaf89d9e6' \
                      '629cff0a217bc2848f1b41cd30d360519'
