from .base import PipBaseRecipe


class WorQRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(WorQRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a46df66b2c3881ad794040bc87806711' \
                      '8be01a245b7f61074cdc3ee94613c812'

        self.name = 'worq'
        self.version = '1.1.0'
