from .base import PipBaseRecipe


class PillowRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PillowRecipe, self).__init__(*args, **kwargs)

        self.name = 'pillow'
        self.version = '4.0.0'
        self.depends = ['libjpeg-turbo', 'libpng']
        self.pydepends = ['olefile']
        self.sha256 = 'ee26d2d7e7e300f76ba7b796014c0401' \
                      '1394d0c4a5ed9a288264a3e443abca50'
