from .base import PipBaseRecipe


class WhooshRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(WhooshRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7ca5633dbfa9e0e0fa400d3151a8a0c4' \
                      'bec53bd2ecedc0a67705b17565c31a83'
        
        self.name = 'Whoosh'
        self.version = '2.7.4'


