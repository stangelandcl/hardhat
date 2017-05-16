from .base import PipBaseRecipe


class CheckManifestRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CheckManifestRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f9b7a3a6071f1991009bfa760f903b6d' \
                      '31f7b852a35d76a1cbbbcd1b22c9f44a'
                
        self.name = 'check-manifest'
        self.version = '0.35'
