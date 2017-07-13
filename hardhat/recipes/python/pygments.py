from .base import PipBaseRecipe


class PygmentsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PygmentsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'dbae1046def0efb574852fab9e90209b' \
                      '23f556367b5a320c0bcb871c77c3e8cc'

        self.name = 'pygments'
        self.version = '2.2.0'
        self.pypi_name = 'Pygments'
