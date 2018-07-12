from .base import PipBaseRecipe


class SetupToolsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SetupToolsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '012adb8e25fbfd64c652e99e7bab5879' \
                      '9a3aaf05d39ab38561f69190a909015f'

        self.name = 'setuptools'
        self.version = '40.0.0'
        self.pydepends = ['appdirs']
