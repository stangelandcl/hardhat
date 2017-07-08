from .base import PipBaseRecipe


class BotoCoreRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(BotoCoreRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'cd96808ff204b7e7c9be62f383bd0da2' \
                      'bdfc6ff14c5e691a81a929788662e10f'

        self.pydepends = ['dateutil', 'docutils', 'jmespath']
        self.name = 'botocore'
        self.version = '1.5.80'
