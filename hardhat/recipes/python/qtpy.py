from .base import PipBaseRecipe


class QtPyRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(QtPyRecipe, self).__init__(*args, **kwargs)
        self.name = 'qtpy'
        self.version = '1.1.2'
