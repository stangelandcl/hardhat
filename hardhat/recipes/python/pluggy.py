from .base import PipBaseRecipe


class PluggyRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PluggyRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'dd841b5d290b252cf645f75f3bd37cee' \
                      'cfa0f36394ab313e4f785fe68a4081a4'
        self.name = 'pluggy'
        self.version = '0.4.0'
