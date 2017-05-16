from .base import PipBaseRecipe


class RepozeLruRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(RepozeLruRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0f7a323bf716d3cb6cb3910cd4fccbee' \
                      '0b3d3793322738566ecce163b01bbd31'
        self.name = 'repoze.lru'
        self.version = '0.6'


