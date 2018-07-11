from .base import PipBaseRecipe


class PytzRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PytzRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ffb9ef1de172603304d9d2819af6f5ec' \
                      'e76f2e85ec10692a524dd876e72bf277'

        self.name = 'pytz'
        self.version = '2018.5'
