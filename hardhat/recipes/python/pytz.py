from .base import PipBaseRecipe


class PytzRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PytzRecipe, self).__init__(*args, **kwargs)

        self.name = 'pytz'
        self.version = '2017.2'
