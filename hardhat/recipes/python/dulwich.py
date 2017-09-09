from .base import PipBaseRecipe


class DulwichRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DulwichRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0c3eccac93823e172b05d57aaeab3d6f' \
                      '03c6c0f1867613606d1909a3ab4100ca'
        self.name = 'dulwich'
        self.depends = []
        self.version = '0.17.3'
