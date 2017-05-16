from .base import PipBaseRecipe


class WebObRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(WebObRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0dc8b30bdbf15d8fd1a967e30ece3357' \
                      'f2f468206354f69213e57b30a63f0039'
        
        self.name = 'WebOb'
        self.version = '1.7.2'


