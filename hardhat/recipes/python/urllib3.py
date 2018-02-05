from .base import PipBaseRecipe


class UrlLib3Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(UrlLib3Recipe, self).__init__(*args, **kwargs)
        self.name = 'urllib3'
        self.version = '1.22'
