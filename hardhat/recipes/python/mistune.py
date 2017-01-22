from .base import PipBaseRecipe


class MistuneRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(MistuneRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '21d0e869df3b9189f248e022f1c9763c' \
                      'f9069e1a2f00676f1f1852bd7f98b713'

        self.name = 'mistune'
        self.version = '0.7.3'
