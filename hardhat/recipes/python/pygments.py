from .base import PipBaseRecipe


class PygmentsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PygmentsRecipe, self).__init__(*args, **kwargs)

        self.name = 'pygments'
        self.version = '2.2.0'
        self.pypi_name = 'Pygments'
