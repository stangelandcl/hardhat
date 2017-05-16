from .base import PipBaseRecipe


class PyramidChameleonRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyramidChameleonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd176792a50eb015d7865b44bd9b24a7b' \
                      'd0489fa9a5cebbd17b9e05048cef9017'

        self.name = 'pyramid_chameleon'
        self.version = '0.3'
        self.pydepends = ['Chameleon']
