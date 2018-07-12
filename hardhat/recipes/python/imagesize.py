from .base import PipBaseRecipe


class ImagesizeRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ImagesizeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5b326e4678b6925158ccc66a9fa3122b' \
                      '6106d7c876ee32d7de6ce59385b96315'

        self.name = 'imagesize'
        self.version = '1.0.0'
