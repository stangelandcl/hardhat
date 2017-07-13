from .base import PipBaseRecipe


class PytzRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PytzRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f5c056e8f62d45ba8215e5cb8f50dfcc' \
                      'b198b4b9fbea8500674f3443e4689589'
        self.name = 'pytz'
        self.version = '2017.2'
