from .base import PipBaseRecipe


class CyclerRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CyclerRecipe, self).__init__(*args, **kwargs)

        self.name = 'cycler'
        self.pydepends = ['six']
        self.version = '0.10.0'
        self.sha256 = 'cd7b2d1018258d7247a71425e' \
                      '9f26463dfb444d411c39569972f4ce586b0c9d8'
