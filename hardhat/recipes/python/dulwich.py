from .base import PipBaseRecipe


class DulwichRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DulwichRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '470d0feec9d4e7aba091c02f62db7f9c' \
                      'c6549ffe3f623a8039f96f584159da05'

        self.name = 'dulwich'
        self.depends = []
        self.version = '0.16.1'
