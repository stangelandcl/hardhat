
from .base import PipBaseRecipe


class PyRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1f9a981438f2acc20470b301a07a4963' \
                      '75641f902320f70e31916fe3377385a9'
        self.name = 'py'
        self.version = '1.4.33'


