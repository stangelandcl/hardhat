from .base import PipBaseRecipe


class DjangoFilterRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DjangoFilterRecipe, self).__init__(*args, **kwargs)

        self.name = 'django-filter'
        self.version = '0.13.0'
        self.pydepends = ['django']
        self.sha256 = 'b4c1614576fe696d1a91d08f100caeff' \
                      'cbc084d93181b3df26f5d4fc0131f0fc'
