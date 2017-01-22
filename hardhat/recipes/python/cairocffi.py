from .base import PipBaseRecipe


class CairoCffiRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CairoCffiRecipe, self).__init__(*args, **kwargs)

        self.name = 'cairocffi'
        self.version = '0.7.2'
        self.depends = ['cairo']
        self.pydepends = ['cffi']
        self.sha256 = 'e42b4256d27bd960cbf3b91a6c55d60' \
                      '2defcdbc2a73f7317849c80279feeb975'
