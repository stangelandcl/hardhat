from .base import PipBaseRecipe


class AppDirsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AppDirsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9e5896d1372858f8dd3344faf4e5014d' \
                      '21849c756c8d5701f78f8a103b372d92'
                
        self.name = 'appdirs'
        self.version = '1.4.3'

