from .base import PipBaseRecipe


class DulwichRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DulwichRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '34f99e575fe1f1e89cca92cec1ddd50b' \
                      '4991199cb00609203b28df9eb83ce259'

        self.name = 'dulwich'
        self.depends = []
        self.pydepends = ['urllib3']
        self.version = '0.19.5'
