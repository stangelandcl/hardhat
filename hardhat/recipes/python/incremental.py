from .base import PipBaseRecipe


class IncrementalRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(IncrementalRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7b751696aaf36eebfab537e458929e19' \
                      '4460051ccad279c72b755a167eebd4b3'
        self.pythons = ['python3']
        self.name = 'incremental'
        self.version = '17.5.0'
