from .base import PipBaseRecipe


class VirtualEnvRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(VirtualEnvRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '02f8102c2436bb03b3ee6dede1919d1d' \
                      'ac8a427541652e5ec95171ec8adbc93a'
                
        self.name = 'virtualenv'
        self.version = '15.1.0'

