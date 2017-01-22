from .base import PipBaseRecipe


class KombuRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(KombuRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '22ab336a17962717a5d9470547e5508d' \
                      '4bcf1b6ec10cd9486868daf4e5edb727'

        self.name = 'kombu'
        self.version = '3.0.35'
        self.pydepends = ['amqp', 'anyjson']
