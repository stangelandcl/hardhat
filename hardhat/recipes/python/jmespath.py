from .base import PipBaseRecipe


class JmesPathRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(JmesPathRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6a81d4c9aa62caf061cb517b4d9ad1dd' \
                      '300374cd4706997aff9cd6aedd61fc64'

        self.name = 'jmespath'
        self.version = '0.9.3'
