from .base import PipBaseRecipe


class HupperRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(HupperRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '25a84e8b8d5dbe938fdc54c0f6a3b77a' \
                      '3d7c6f08f22ee940256b654e95dde4b8'
                
        self.name = 'hupper'
        self.version = '0.5'
