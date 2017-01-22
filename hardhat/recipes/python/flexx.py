from .base import PipBaseRecipe


class FlexxRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(FlexxRecipe, self).__init__(*args, **kwargs)

        self.name = 'flexx'
        self.version = '0.4.1'
        self.pydepends = ['tornado']
        self.sha256 = '54be868f01d943018d0907821f2562f6' \
                      'eb31c568b3932abfd8518f75c29b8be1'
