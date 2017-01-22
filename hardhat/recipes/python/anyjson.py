from .base import PipBaseRecipe


class AnyjsonRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AnyjsonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '37812d863c9ad3e35c0734c42e0bf032' \
                      '0ce8c3bed82cd20ad54cb34d158157ba'

        self.name = 'anyjson'
        self.version = '0.3.3'
