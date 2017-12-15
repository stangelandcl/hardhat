from .base import PipBaseRecipe


class ClickRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ClickRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f15516df478d5a56180fbf80e68f2060' \
                      '10e6d160fc39fa508b65e035fd75130b'

        self.name = 'click'
        self.version = '6.7'
