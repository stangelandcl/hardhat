from .base import PipBaseRecipe


class XlwtRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(XlwtRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c59912717a9b28f1a3c2a98fd6074101' \
                      '4b06b043936dcecbc113eaaada156c88'

        self.name = 'xlwt'
        self.version = '1.3.0'
