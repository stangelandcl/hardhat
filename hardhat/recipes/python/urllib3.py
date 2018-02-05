from .base import PipBaseRecipe


class UrlLib3Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(UrlLib3Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'cc44da8e1145637334317feebd728bd8' \
                      '69a35285b93cbb4cca2577da7e62db4f'

        self.name = 'urllib3'
        self.version = '1.22'
