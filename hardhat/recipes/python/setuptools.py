from .base import PipBaseRecipe


class SetupToolsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SetupToolsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1e55496ca8058db68ae12ac29a985d1e' \
                      'e2c2483a5901f7692fb68fa2f9a250fd'
                
        self.name = 'setuptools'
        self.version = '35.0.2'
        self.pydepends = ['appdirs', 'packaging']
