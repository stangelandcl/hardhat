from .base import PipBaseRecipe


class SetupToolsScmRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SetupToolsScmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1191f2a136b5e86f7ca8ab00a97ef7ae' \
                      'f997131f1f6d4971be69a1ef387d8b40'

        self.name = 'setuptools_scm'
        self.version = '3.1.0'
        self.pydepends = ['setuptools']
