from .base import PipBaseRecipe


class PytzRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PytzRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7016b2c4fa075c564b81c37a252a5fcc' \
                      'f60d8964aa31b7f5eae59aeb594ae02b'

        self.name = 'pytz'
        self.version = '2016.10'
