from .base import PipBaseRecipe


class DjangoRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DjangoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0db89374b691b9c8b057632a6cd64b18' \
                      'd08db2f4d63b4d4af6024267ab965f8b'

        self.pydepends = ['cchardet', 'chardet']
        self.name = 'django'
        self.version = '1.10.5'
