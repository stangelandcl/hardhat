from .base import PipBaseRecipe


class PasteDeployRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PasteDeployRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd5858f89a255e6294e63ed46b73613c5' \
                      '6e3b9a2d82a42f1df4d06c8421a9e3cb'
        self.name = 'PasteDeploy'
        self.version = '1.5.2'
