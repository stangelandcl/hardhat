from .base import PipBaseRecipe


class SupervisorRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SupervisorRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3176fb8a78c60164020e252e4a2b50b0' \
                      '39cfec1f410b4562a843b66186188652'

        self.pythons = ['python2']
        self.name = 'supervisor'
        self.version = '3.3.0'
        self.pydepends = ['meld3']
