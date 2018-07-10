from .base import PipBaseRecipe


class YarlTimeoutRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(YarlTimeoutRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c8cbc21bbfa1dd7d5386d48cc814fe3d' \
                      '35b80f60299cdde9279046f399c3b0d8'

        self.pythons = ['python3']
        self.name = 'yarl'
        self.pydepends = ['idna']
        self.version = '1.2.6'
