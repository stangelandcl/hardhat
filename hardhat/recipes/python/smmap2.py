from .base import PipBaseRecipe


class Smmap2Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Smmap2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c7530db63f15f09f8251094b22091298' \
                      'e82bf6c699a6b8344aaaef3f2e1276c3'
        self.name = 'smmap2'
        self.version = '2.0.3'
