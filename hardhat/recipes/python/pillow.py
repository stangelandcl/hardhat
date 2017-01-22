from .base import PipBaseRecipe


class PillowRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PillowRecipe, self).__init__(*args, **kwargs)

        self.name = 'pillow'
        self.version = '3.2.0'
        self.depends = ['libjpeg-turbo', 'libpng']
        self.sha256 = '64b0a057210c480aea99406c9391180cd' \
                      '866fc0fd8f0b53367e3af21b195784a'
