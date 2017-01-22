from .base import PipBaseRecipe


class EntryPointsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(EntryPointsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0a0685962ee5ac303f470acbb659f0f9' \
                      '7aef5b9deb6b85d059691c706ef6e45e'

        self.name = 'entrypoints'
        self.version = '0.2.2'
