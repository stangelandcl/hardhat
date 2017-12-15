from .base import PipBaseRecipe


class SetupToolsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SetupToolsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9c671a6291a5b1171fb9da81665eb4f9' \
                      '625c7dbddc613d82abdc6002a4bce896'

        self.name = 'setuptools'
        self.version = '38.2.4'
        self.pydepends = ['appdirs', 'packaging']
