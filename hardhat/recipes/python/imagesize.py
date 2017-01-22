from .base import PipBaseRecipe


class ImagesizeRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ImagesizeRecipe, self).__init__(*args, **kwargs)

        self.name = 'imagesize'
        self.version = '0.7.1'
        self.sha256 = '0ab2c62b87987e3252f89d30b7cedbec' \
                      '12a01af9274af9ffa48108f2c13c6062'
