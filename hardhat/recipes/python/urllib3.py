from .base import PipBaseRecipe


class UrlLib3Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(UrlLib3Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a68ac5e15e76e7e5dd2b8f94007233e0' \
                      '1effe3e50e8daddf69acfd81cb686baf'

        self.name = 'urllib3'
        self.version = '1.23'
