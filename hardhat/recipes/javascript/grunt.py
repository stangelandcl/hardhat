from .base import NpmBaseRecipe


class GruntRecipe(NpmBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(GruntRecipe, self).__init__(*args, **kwargs)
        self.name = 'grunt'
        self.version = '1.0.1'
