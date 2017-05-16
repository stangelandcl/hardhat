from .base import PipBaseRecipe


class ExecNetRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ExecNetRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f66dd4a7519725a1b7e14ad9ae7d3df8' \
                      'e09b2da88062386e08e941cafc0ef3e6'
        self.name = 'execnet'
        self.version = '1.4.1'
        self.pydepends = ['apipkg']

