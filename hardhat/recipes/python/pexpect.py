from .base import PipBaseRecipe


class PexpectRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PexpectRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3d132465a75b57aa818341c6521392a0' \
                      '6cc660feb3988d7f1074f39bd23c9a92'

        self.name = 'pexpect'
        self.version = '4.2.1'
        self.pydepends = ['ptyprocess']
