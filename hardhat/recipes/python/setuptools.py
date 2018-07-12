from .base import PipBaseRecipe


class SetupToolsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SetupToolsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c5484e13b89927b44fd15897f7ce19dd' \
                      'ed8e7f035466a4fa7b946c0bdd86edd7'

        self.name = 'setuptools'
        self.version = '39.1.0'
        self.pydepends = ['appdirs']
