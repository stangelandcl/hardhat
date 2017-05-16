from .base import PipBaseRecipe


class ChameleonRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ChameleonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'caa3b79eed61038582a7bbb35bc67d20' \
                      '85d3d2497a94f890228c2937d87dc167'

        self.name = 'Chameleon'
        self.version = '3.1'
