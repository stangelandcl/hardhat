from .base import OpamBaseRecipe


class FramacRecipe(OpamBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(FramacRecipe, self).__init__(*args, **kwargs)
        self.name = 'frama-c-base'
        self.version = '20170501'
        self.depends = ['opam']
